from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для в9алидации. Вызывается при создании и обновлении."""
        # print(data['status'])
        # TODO: добавь9те требуемую валидацию

        print(self.context["request"].user)
        if 'OPEN' in data or 'title' in data:
            advertisement = Advertisement.objects.all()
            sr = []
            for t in range(len(advertisement)):

                if advertisement[t].status == 'OPEN' and advertisement[t].creator == self.context["request"].user:
                    sr.append(advertisement[t].status)

                if len(sr) >= 10:
                    raise serializers.ValidationError(f'У вас больше 10 открытых обьявлений, закройте не нужные!')
            sr.clear()

        return data
