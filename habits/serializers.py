from rest_framework import serializers
from .models import Habit
from django.core.exceptions import ValidationError


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('user',)  # Поле user автоматически заполняется

    def validate(self, attrs):
        """ Все кастомные валидации из ТЗ """

        # Валидатор 1: Исключить одновременный выбор связанной привычки и вознаграждения
        related_habit = attrs.get('related_habit')
        reward = attrs.get('reward')
        if related_habit and reward:
            raise serializers.ValidationError("Нельзя одновременно выбирать связанную привычку и вознаграждение.")

        # Валидатор 2: В связанные привычки могут попадать только привычки с признаком приятной привычки
        if related_habit and not related_habit.is_pleasant:
            raise serializers.ValidationError("В связанные привычки можно добавлять только приятные привычки.")

        # Валидатор 3: У приятной привычки не может быть вознаграждения или связанной привычки
        is_pleasant = attrs.get('is_pleasant', self.instance.is_pleasant if self.instance else False)
        if is_pleasant:
            if reward:
                raise serializers.ValidationError("У приятной привычки не может быть вознаграждения.")
            if related_habit:
                raise serializers.ValidationError("У приятной привычки не может быть связанной привычки.")

        # Валидатор 4: Время на выполнение должно быть не больше 120 секунд
        duration = attrs.get('duration')
        if duration and duration > 120:
            raise serializers.ValidationError("Время выполнения не может быть больше 120 секунд.")

        return attrs
