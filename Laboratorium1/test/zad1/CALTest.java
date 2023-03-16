package zad1;

import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.*;

public class CALTest {
    private CAL cal;

    @BeforeAll
    public static void setUp() {
        System.out.println("@BeforeAll executed");
    }

    @BeforeEach
    void setupThis() {
        cal = new CAL();
        System.out.println("@BeforeEach executed");
    }

    @Test
    void testSUM() {
        int sum = cal.SUM(2, 1);
        assertEquals(3, sum);
        System.out.println("Test1");
    }

    @Test
    void testSUM1() {
        int sum = cal.SUM(4, -7);
        assertEquals(-3, sum);
        System.out.println("Test2");
    }

    @Test
    void testSUB() {
        int sub = cal.SUB(3, -5);
        assertEquals(8, sub);
        System.out.println("Test3");
    }

    @Test
    void testSUB1() {
        int sub = cal.SUB(10, 4);
        assertEquals(6, sub);
        System.out.println("Test4");
    }

    @Test
    void testDIV() {
        int div = cal.DIV(4, 2);
        assertEquals(2, div);
        System.out.println("Test5");
    }

    @Test
    void testDIV1() {
        int div = cal.DIV(7, -2);
        assertEquals(-3, div);
        System.out.println("Test6");
    }

    @Test
    void  testMUL() {
        int mul = cal.MUL(5, 3);
        assertEquals(15, mul);
        System.out.println("Test7");
    }

    @Test
    void testMUL1() {
        int mul = cal.MUL(-2, 8);
        assertEquals(-16, mul);
        System.out.println("Test8");
    }

    @Test
    void testNotEquals() {
        int mul = cal.MUL(4, 4);
        int div = cal.DIV(4, 4);
        assertNotEquals(mul, div);
        System.out.println("Test9");
    }

    @Test
    void throwException() {
        Throwable exception = assertThrows(
                IllegalArgumentException.class, () -> cal.DIV(3, 0)
        );
        assertEquals("You can't divide by 0", exception.getMessage());
        System.out.println("Test10");
    }
    @AfterEach
    void tearThis() {
        System.out.println("@AfterEach executed");
    }

    @AfterAll
    public static void tearDown() {
        System.out.println("@AfterAll executed");
    }

}
