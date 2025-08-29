/**
 * Claude Code + GLM-4.5 集成测试文件
 * 
 * 使用说明：
 * 1. 打开此文件
 * 2. 按 Cmd+Shift+P 打开命令面板
 * 3. 输入 "Claude" 查看可用命令
 * 4. 选择 "Claude Dev: Start New Task" 开始与 GLM-4.5 交互
 * 
 * 测试场景：
 * - 请 Claude 帮你完善这个用户管理类
 * - 让 Claude 解释代码逻辑
 * - 要求 Claude 优化性能
 * - 让 Claude 添加错误处理
 */

interface User {
  id: string;
  name: string;
  email: string;
  createdAt: Date;
}

class UserManager {
  private users: User[] = [];

  constructor() {
    console.log('用户管理器已初始化');
  }

  // TODO: 请 Claude Code + GLM-4.5 帮助完善以下方法

  /**
   * 添加用户
   * @param userData 用户数据
   */
  addUser(userData: Omit<User, 'id' | 'createdAt'>): User {
    // 请 Claude 帮助实现这个方法
    throw new Error('待实现');
  }

  /**
   * 根据 ID 查找用户
   * @param id 用户 ID
   */
  findUserById(id: string): User | undefined {
    // 请 Claude 帮助实现这个方法
    throw new Error('待实现');
  }

  /**
   * 更新用户信息
   * @param id 用户 ID
   * @param updates 更新数据
   */
  updateUser(id: string, updates: Partial<Omit<User, 'id' | 'createdAt'>>): User | null {
    // 请 Claude 帮助实现这个方法
    throw new Error('待实现');
  }

  /**
   * 删除用户
   * @param id 用户 ID
   */
  deleteUser(id: string): boolean {
    // 请 Claude 帮助实现这个方法
    throw new Error('待实现');
  }

  /**
   * 获取所有用户
   */
  getAllUsers(): User[] {
    // 请 Claude 帮助实现这个方法
    throw new Error('待实现');
  }
}

// 测试代码 - 请 Claude 帮助完善
const userManager = new UserManager();

// 请 Claude 帮助编写测试用例
console.log('开始测试用户管理器...');

export { User, UserManager };
