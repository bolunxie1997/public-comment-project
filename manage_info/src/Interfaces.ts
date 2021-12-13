interface FileItem {
    uid: string;
    name?: string;
    status?: string;
    response?: string;
    percent?: number;
    url?: string;
    preview?: string;
    originFileObj?: any;
}

interface FileInfo {
    file: FileItem;
    fileList: FileItem[];
}


interface FormState {
    pass: string;
    checkPass: string;
    username: String,
    age: number | undefined;
}
interface UserItem {
    id: string | number;
    username: string;
    age: number;
    gender: string;
    type: number | string,
    ctime: string | Date
}

interface CommentItem {
    id: string | number;
    content: string;
    rating: number;
    imgs: [string];
    shop: {
        name: string,
        type: string
    },
    state: Number,
    author: {
        username: string,
        avatar: string,
    },
    replies_length: number | string,
    ctime: string | Date
}
interface ShopItem {
    id: string | number;
    name: string;
    address: string,
    desc: string,
    imgs: [string];
    owner: {
        username: string,
        avatar: string,
    },
    state: Number,
    type: string,
    comments_length: number | string,
    average_rating: number;
    ctime: string | Date
}
interface ReplyItem {
    id: string | number;
    content: string;
    author: {
        username: string,
        avatar: string,
    },
    shop: {
        id: string | Number,
        name: string,
        imgs: string
    },
    comment: {
        author: {
            username: string,
            avatar: string,
        },
        content:string
    },
    state: Number,
    ctime: string | Date
}

export {
    FileInfo,
    FileItem,
    FormState,
    UserItem,
    CommentItem,
    ShopItem,
    ReplyItem
}


