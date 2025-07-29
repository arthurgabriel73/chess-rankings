class CategoryValidator:
    valid_categories = ['bullet', 'blitz', 'rapid', 'classical', 'ultraBullet']

    @staticmethod
    def validate_category(category: str):
        if (
            not category
            or not isinstance(category, str)
            or not CategoryValidator.valid_categories.__contains__(category.lower())
        ):
            raise ValueError(f'Invalid category: must be one of: {", ".join(CategoryValidator.valid_categories)}')
