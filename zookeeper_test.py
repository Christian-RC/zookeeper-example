import unittest
from zookeeper import Ztree


class TestZookeeper(unittest.TestCase):

    def test_crear_znodes(self):
        tree = Ztree()
        print(
            "\n\n **************************** TEST: Ceando znodes ***************************")
        tree.create('/node1', 'Dato1', True, True, 10, '/')
        tree.create('/node1/node1_1', 'Dato1_1', True, True, 10, '/')
        tree.create('/node2', 'Dato2', True, True, 10, '/')
        tree.showTree()
        self.assertEqual(tree.getData('/node1'), 'Dato1')
        self.assertEqual(tree.getData('/node1/node1_1'), 'Dato1_1')
        self.assertEqual(tree.getData('/node2'), 'Dato2')

    def test_no_se_puede_crear(self):
        print("\n\n **************************** TEST: No se puede crear znodes ****************************")
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'Dato3', True, True, 10, None)
        tree.showTree()

    def test_ver_arbol(self):
        tree = Ztree()
        print(
            "\n\n **************************** TEST: Ver árbol ****************************")
        tree.create('/node1', 'Dato1', True, True, 10, '/')
        tree.create('/node1/node1_1', 'Dato1_1', True, True, 10, '/')
        tree.create('/node2', 'Dato2', True, True, 10, '/')
        tree.create('/node2/node2_1', 'Dato2_1', True, True, 10, '/')
        tree.create('/node2/node2_2', 'Dato2_2', True, True, 10, '/')
        tree.showTree()

    def test_ver_nodo_existente(self):
        tree = Ztree()
        print("\n\n **************************** TEST: Ver nodo existente -> /node1 ****************************")
        tree.create('/node1', 'Dato1', True, True, 10, '/')
        tree.showNode('/node1')
        self.assertEqual(tree.getData('/node1'), 'Dato1')

    def test_ver_nodo_NO_existente(self): 
        tree = Ztree()
        print("\n\n **************************** TEST: Ver nodo NO existente -> /node1/node1_1 ****************************")
        tree.create('/node1', 'Dato1', True, True, 10, '/')
        tree.showTree()
        self.assertIsNone(tree.getData('/node1/node1_1'))

    def test_actualizar_contenido(self): 
        tree = Ztree()
        print("\n\n **************************** TEST: actualizar contenido ****************************")
        tree.create('/node1', 'Dato1', True, True, 10, '/')
        print("Contenido ANTES de actualizar: ", tree.getData('/node1'))
        tree.setData('/node1', 'Dato1_actualizado')
        print("Contenido DESPUÉS de actualizar: ", tree.getData('/node1'))
        self.assertEqual(tree.getData('/node1'), 'Dato1_actualizado')

    def test_borrar_nodo(self): 
        tree = Ztree()
        print("\n\n **************************** TEST: borrar nodo ****************************")
        tree.create('/node1', 'Dato1', True, True, 10, '/')
        tree.create('/node1/node1_1', 'Dato1_1', True, True, 10, '/')
        print(" Árbol ANTES de borrar nodo: ")
        tree.showTree()
        tree.delete('/node1/node1_1', 0)
        print("\n Árbol DESPUÉS de borrar nodo: ")
        tree.showTree()

    def test_verificar_nodo(self):
        tree = Ztree()
        print(
            "\n\n **************************** TEST: verificar nodo ****************************")
        tree.create('/node1', 'Dato1', True, True, 10, '/')
        if (tree.exist('/node1')):
            print("El nodo ha sido encontrado")


if __name__ == '__main__':
    unittest.main()