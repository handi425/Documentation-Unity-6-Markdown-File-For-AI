[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [Application](Application.html).Quit

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

## Declaration

public static void Quit();

### Parameters

exitCode | An optional exit code to return when the player application terminates on Windows, Mac and Linux. Defaults to 0.  
---|---  
  
### Description

Quits the player application.

Shut down the running application. The Application.Quit call is ignored in the
Editor.  
  
If you want to use `Application.Quit` when running Unity inside another
application, refer to [Unity as a Library](../Manual/UnityasaLibrary.html)
documentation.  
  
On the Web platform, `Application.Quit` stops the Web Player but doesn't
affect the web page front end. For ways to implement `Application.Quit` and
manage resource cleanup, refer to examples in the [web
templates](../Manual/webgl-templates.html).  
  
Android and iOS platforms have their own dedicated interfaces to hide and
close applications, which might be the preferred way to close applications for
some users. Therefore, it's not recommended to create your own way of shutting
down with `Application.Quit` to prevent inconsistent user experience between
your application and these platform interfaces. If you must programmatically
quit an Android application, you can instead move the application to the
background via
[Activity.moveTaskToBack](https://developer.android.com/reference/android/app/Activity#moveTaskToBack\(boolean\)).
For more information, refer to [Quit a Unity Android
application](../Manual/android-quit.html).  
  
For iOS platform, in most cases the termination of application should be left
at the user's discretion. Calling `Application.Quit` method in iOS Player
might appear to the user that the application has crashed. For more
information, refer to [Apple Technical Page
qa1561](https://developer.apple.com/library/archive/qa/qa1561/_index.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Quits the player when the user hits escape  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKey](Input.GetKey.html)("escape"))
            {
                [Application.Quit](Application.Quit.html)();
            }
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

