-- DROP PROCEDURE SP_STOCK_PROD;

/* PROCEDIMIENTO ALMACENADO QUE DISMINUYE STOCK */
CREATE OR REPLACE PROCEDURE SP_STOCK_PROD
(p_id_prod NUMBER, p_cant NUMBER) IS
    cant_actual NUMBER(8); 
BEGIN
    SELECT stock INTO cant_actual FROM producto_producto WHERE id_producto = p_id_prod;
    UPDATE producto_producto 
        SET stock = (cant_actual - p_cant) 
    WHERE id_producto = p_id_prod ;
END;

/* TRIGGER QUE LLAMA AL PROCEDIMIENTO ANTERIOR*/

CREATE OR REPLACE TRIGGER TRG_DISMINUYE_STOCK
AFTER INSERT ON carrito_detalle_compra
FOR EACH ROW
BEGIN
    SP_STOCK_PROD(:NEW.id_producto_id,:NEW.cantidad);
END;