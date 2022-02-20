import uuid

from fastapi import Request
from fastapi.responses import JSONResponse


class ExternalError(Exception):
    def __init__(self):
        self.status = 500
        self.message = 'An error occurred in the integration API'


class ResourceAlreadySynced(Exception):
    def __init__(self, resource: str):
        self.status = 400
        self.message = f'{resource.title()} already synced'


class ResourceNotFound(Exception):
    def __init__(self, resource: str, id_: uuid.UUID):
        self.status = 404
        self.message = f'{resource.title()} with id {id_} not found'


def external_error(request: Request, exc: ExternalError):
    return JSONResponse(
        status_code=exc.status,
        content={
            'message': exc.message,
            'success': False,
        }
    )


def resource_already_synced(request: Request, exc: ResourceAlreadySynced):
    return JSONResponse(
        status_code=exc.status,
        content={
            'message': exc.message,
            'success': False,
        }
    )


def resource_not_found(request: Request, exc: ResourceNotFound):
    return JSONResponse(
        status_code=exc.status,
        content={
            'message': exc.message,
            'success': False,
        }
    )
