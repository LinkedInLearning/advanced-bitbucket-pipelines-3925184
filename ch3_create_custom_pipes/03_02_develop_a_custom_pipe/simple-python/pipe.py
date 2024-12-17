from bitbucket_pipes_toolkit import Pipe

variables = {
  'NAME': {'type': 'string', 'required': True},
  'DEBUG': {'type': 'boolean', 'required': False, 'default': False}
}

pipe = Pipe(schema=variables)
name = pipe.get_variable('NAME')

pipe.log_info("Executing the pipe...")
pipe.log_info("Hello, " + name)

pipe.success(message="Success!")