# coding: utf-8

"""
    launch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
from datetime import date, datetime  # noqa: F401

import frozendict  # noqa: F401
import typing_extensions  # noqa: F401

from launch.api_client import schemas  # noqa: F401


class CreateFineTuneRequest(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "training_file",
            "hyperparameters",
            "model",
        }

        class properties:
            class hyperparameters(schemas.DictSchema):
                class MetaOapg:
                    class additional_properties(
                        schemas.ComposedSchema,
                    ):
                        class MetaOapg:
                            any_of_0 = schemas.StrSchema
                            any_of_1 = schemas.IntSchema
                            any_of_2 = schemas.NumberSchema

                            @classmethod
                            @functools.lru_cache()
                            def any_of(cls):
                                # we need this here to make our import statements work
                                # we must store _composed_schemas in here so the code is only run
                                # when we invoke this method. If we kept this at the class
                                # level we would get an error because the class level
                                # code would be run when this module is imported, and these composed
                                # classes don't exist yet because their module has not finished
                                # loading
                                return [
                                    cls.any_of_0,
                                    cls.any_of_1,
                                    cls.any_of_2,
                                ]

                        def __new__(
                            cls,
                            *_args: typing.Union[
                                dict,
                                frozendict.frozendict,
                                str,
                                date,
                                datetime,
                                uuid.UUID,
                                int,
                                float,
                                decimal.Decimal,
                                bool,
                                None,
                                list,
                                tuple,
                                bytes,
                                io.FileIO,
                                io.BufferedReader,
                            ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[
                                schemas.AnyTypeSchema,
                                dict,
                                frozendict.frozendict,
                                str,
                                date,
                                datetime,
                                uuid.UUID,
                                int,
                                float,
                                decimal.Decimal,
                                None,
                                list,
                                tuple,
                                bytes,
                            ],
                        ) -> "additional_properties":
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                                **kwargs,
                            )

                def __getitem__(self, name: typing.Union[str,]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)

                def get_item_oapg(self, name: typing.Union[str,]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)

                def __new__(
                    cls,
                    *_args: typing.Union[
                        dict,
                        frozendict.frozendict,
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[
                        MetaOapg.additional_properties,
                        dict,
                        frozendict.frozendict,
                        str,
                        date,
                        datetime,
                        uuid.UUID,
                        int,
                        float,
                        decimal.Decimal,
                        bool,
                        None,
                        list,
                        tuple,
                        bytes,
                        io.FileIO,
                        io.BufferedReader,
                    ],
                ) -> "hyperparameters":
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            model = schemas.StrSchema
            training_file = schemas.StrSchema
            suffix = schemas.StrSchema
            validation_file = schemas.StrSchema
            wandb_config = schemas.DictSchema
            __annotations__ = {
                "hyperparameters": hyperparameters,
                "model": model,
                "training_file": training_file,
                "suffix": suffix,
                "validation_file": validation_file,
                "wandb_config": wandb_config,
            }

    training_file: MetaOapg.properties.training_file
    hyperparameters: MetaOapg.properties.hyperparameters
    model: MetaOapg.properties.model

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hyperparameters"]) -> MetaOapg.properties.hyperparameters:
        ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model:
        ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["training_file"]) -> MetaOapg.properties.training_file:
        ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suffix"]) -> MetaOapg.properties.suffix:
        ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validation_file"]) -> MetaOapg.properties.validation_file:
        ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wandb_config"]) -> MetaOapg.properties.wandb_config:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "hyperparameters",
                "model",
                "training_file",
                "suffix",
                "validation_file",
                "wandb_config",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hyperparameters"]) -> MetaOapg.properties.hyperparameters:
        ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model:
        ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["training_file"]) -> MetaOapg.properties.training_file:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["suffix"]
    ) -> typing.Union[MetaOapg.properties.suffix, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["validation_file"]
    ) -> typing.Union[MetaOapg.properties.validation_file, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["wandb_config"]
    ) -> typing.Union[MetaOapg.properties.wandb_config, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "hyperparameters",
                "model",
                "training_file",
                "suffix",
                "validation_file",
                "wandb_config",
            ],
            str,
        ],
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        training_file: typing.Union[
            MetaOapg.properties.training_file,
            str,
        ],
        hyperparameters: typing.Union[
            MetaOapg.properties.hyperparameters,
            dict,
            frozendict.frozendict,
        ],
        model: typing.Union[
            MetaOapg.properties.model,
            str,
        ],
        suffix: typing.Union[MetaOapg.properties.suffix, str, schemas.Unset] = schemas.unset,
        validation_file: typing.Union[MetaOapg.properties.validation_file, str, schemas.Unset] = schemas.unset,
        wandb_config: typing.Union[
            MetaOapg.properties.wandb_config, dict, frozendict.frozendict, schemas.Unset
        ] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[
            schemas.AnyTypeSchema,
            dict,
            frozendict.frozendict,
            str,
            date,
            datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            None,
            list,
            tuple,
            bytes,
        ],
    ) -> "CreateFineTuneRequest":
        return super().__new__(
            cls,
            *_args,
            training_file=training_file,
            hyperparameters=hyperparameters,
            model=model,
            suffix=suffix,
            validation_file=validation_file,
            wandb_config=wandb_config,
            _configuration=_configuration,
            **kwargs,
        )
