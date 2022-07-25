from desafio_machine_learning_engineer.pipelines.model_inference.nodes import format_input

class TestFormat:
    """
    Classe para teste da formatacao do payload
    """
    def test_format_ok(self):
        
        """
        Testa se o format esta funcionando corretamente
        para uma entrada OK
        """
        
        test_payload = {
            "products": [
                {
                    "title": "Lembrancinha"
                },
                {
                    "title": "Carrinho de Bebê"
                },
                {
                    "title": "Teste 123"
                }
            ]
        }
        
        output = format_input(test_payload)
        
        assert output["status"] == 200
        
        assert isinstance(output["products"], list)
        
        # Checa se o output e valido
        assert output == {
            "products": [
                "Lembrancinha",
                "Carrinho de Bebê",
                "Teste NUM"
            ],
            "status": 200
        }
        
        
        
    def test_format_bad_key1(self):
        
        """
        Testa se fornece resultado correto para uma key errada
        """
        
        test_payload = {
            "foo": [
                {
                    "title": "Lembrancinha"
                },
                {
                    "title": "Carrinho de Bebê"
                },
            ]
        }
        
        output = format_input(test_payload)
        
        assert output["status"] == 400
        
    def test_format_bad_key2(self):
        
        """
        Testa se fornece resultado correto para uma key errada
        """
        
        test_payload = {
            "products": [
                {
                    "bar": "Lembrancinha"
                },
                {
                    "title": "Carrinho de Bebê"
                },
            ]
        }
        
        output = format_input(test_payload)
        
        assert output["status"] == 400
        
    def test_format_list(self):
        
        """
        Testa se fornece resultado correto para uma entrada lista
        """
        
        test_payload = {
            "products": [
                {
                    "title": ["Lembrancinha"]
                },
                {
                    "title": "Carrinho de Bebê"
                },
            ]
        }
        
        output = format_input(test_payload)
        
        assert output["status"] == 400
        
    def test_format_int(self):
        
        """
        Testa se fornece resultado correto para uma entrada int
        """
        
        test_payload = {
            "products": [
                {
                    "title": 123
                },
                {
                    "title": "Carrinho de Bebê"
                },
            ]
        }
        
        output = format_input(test_payload)
        
        assert output["status"] == 400
        
    def test_format_dict(self):
        
        """
        Testa se fornece resultado correto para uma entrada dict
        """
        
        test_payload = {
            "products": [
                {
                    "title": {"Lembrancinha": "Bebê"}
                },
                {
                    "title": "Carrinho de Bebê"
                },
            ]
        }
        
        output = format_input(test_payload)
        
        assert output["status"] == 400
        