from bitbucket_pipes_toolkit import Pipe, get_logger

logger = get_logger()

schema = {
  'CUSTOMER_ID': {'type': 'string', 'required': True},
  'DEBUG': {'type': 'boolean', 'required': False, 'default': False}
}


class DemoPipe(Pipe):
    def run(self):
        super().run()

        logger.info('Executing the pipe...')
        customer_id = self.get_variable('CUSTOMER_ID')

        print(customer_id)

        self.success(message=f"CUSTOMER_ID {customer_id} processed successfully!")


if __name__ == '__main__':
    pipe = DemoPipe(pipe_metadata='/pipe.yml', schema=schema)
    pipe.run()
