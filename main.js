// ===============================
// Mon: Ngon ngu phat trien moi
// Ngon ngu: JavaScript (file.js)
// Sinh vien: Nguyen Khac Huy
// Lop: 22DTHC1
// MSSV: 2280601183
// ===============================

// De bai: Product gom cac thuoc tinh:
// id, name, price, quantity, category, isAvailable (true/false)

// ---------- Cau 1: Khai bao constructor function Product ----------
function Product(id, name, price, quantity, category, isAvailable) {
  this.id = id;                 // ma san pham
  this.name = name;             // ten san pham
  this.price = price;           // gia san pham
  this.quantity = quantity;     // so luong ton kho
  this.category = category;     // danh muc san pham
  this.isAvailable = isAvailable; // trang thai ban (true/false)
}

// Ham tien ich in gia tien (VND)
function formatVND(value) {
  // Dung Intl neu co; neu khong thi fallback
  try {
    return new Intl.NumberFormat("vi-VN", { style: "currency", currency: "VND" }).format(value);
  } catch {
    return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".") + " VND";
  }
}

function statusText(isAvailable) {
  return isAvailable ? "Dang ban" : "Ngung ban";
}

console.log("===== BAI TAP JS - Product =====");

// ---------- Cau 2: Khoi tao mang products gom it nhat 6 san pham, it nhat 2 danh muc ----------
const products = [
  new Product(1, "Laptop Gaming", 35900000, 5, "Electronics", true),
  new Product(2, "Ban phim co", 1290000, 0, "Accessories", true),
  new Product(3, "Chuot khong day", 790000, 18, "Accessories", true),
  new Product(4, "Man hinh 27 inch", 4990000, 7, "Electronics", true),
  new Product(5, "Tai nghe", 990000, 12, "Accessories", false),
  new Product(6, "Dien thoai", 31900000, 2, "Electronics", true),
];

console.log("\n(Cau 2) Mang products:");
console.table(products);

// ---------- Cau 3: Tao mang moi chi chua name, price cua moi san pham ----------
const namePriceList = products.map(p => ({ name: p.name, price: p.price }));
console.log("\n(Cau 3) Mang moi chi chua name, price:");
console.table(namePriceList);

// ---------- Cau 4: Loc ra cac san pham con hang trong kho (quantity > 0) ----------
const inStockProducts = products.filter(p => p.quantity > 0);
console.log("\n(Cau 4) San pham con hang (quantity > 0):");
console.table(inStockProducts);

// ---------- Cau 5: Kiem tra co it nhat 1 san pham co gia tren 30.000.000 hay khong ----------
const hasOver30M = products.some(p => p.price > 30000000);
console.log(`\n(Cau 5) Co it nhat 1 san pham gia > 30.000.000? => ${hasOver30M}`);

// ---------- Cau 6: Kiem tra tat ca san pham thuoc danh muc "Accessories" co dang duoc ban (isAvailable = true) hay khong ----------
const accessories = products.filter(p => p.category === "Accessories");
const allAccessoriesAvailable = accessories.every(p => p.isAvailable === true);
console.log(`\n(Cau 6) Tat ca san pham 'Accessories' dang ban? => ${allAccessoriesAvailable}`);
console.log("(Danh sach Accessories):");
console.table(accessories);

// ---------- Cau 7: Tinh tong gia tri kho hang (Gia tri kho = price * quantity) ----------
const totalInventoryValue = products.reduce((sum, p) => sum + (p.price * p.quantity), 0);
console.log(`\n(Cau 7) Tong gia tri kho hang = ${formatVND(totalInventoryValue)}`);

// ---------- Cau 8: Dung for...of duyet mang products va in: Ten san pham - Danh muc - Trang thai ----------
console.log("\n(Cau 8) for...of in: Ten san pham - Danh muc - Trang thai");
for (const p of products) {
  console.log(`${p.name} - ${p.category} - ${statusText(p.isAvailable)}`);
}

// ---------- Cau 9: Dung for...in de in ra ten thuoc tinh va gia tri tuong ung ----------
console.log("\n(Cau 9) for...in in ra ten thuoc tinh va gia tri tuong ung (san pham dau tien):");
const firstProduct = products[0];
for (const key in firstProduct) {
  if (Object.prototype.hasOwnProperty.call(firstProduct, key)) {
    console.log(`${key}: ${firstProduct[key]}`);
  }
}

// ---------- Cau 10: Lay danh sach ten cac san pham dang ban va con hang ----------
const sellingAndInStockNames = products
  .filter(p => p.isAvailable === true && p.quantity > 0)
  .map(p => p.name);

console.log("\n(Cau 10) Ten san pham dang ban va con hang:");
console.log(sellingAndInStockNames);

// Ket thuc
console.log("\n===== END =====");
