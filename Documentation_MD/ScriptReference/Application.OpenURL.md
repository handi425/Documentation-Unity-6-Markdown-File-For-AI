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

#  [Application](Application.html).OpenURL

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

public static void OpenURL(string url);

### Parameters

url | The URL to open.  
---|---  
  
### Description

Opens the URL specified, subject to the permissions and limitations of your
app’s current platform and environment.

This is handled in different ways depending on the nature of the URL, and with
different security restrictions, depending on the runtime platform.  
  
**Note** : The `OpenURL` method can be used to open more than just web pages;
therefore, ensure that you're aware of the security implications involved
before using this method. This method is used to open HTTP and HTTPS (web
page) URLs. If you provide a web page address as the parameter for this
method, the web page opens in the default browser and display the browser
application in the front.  
  
In addition to the HTTP protocol used for web browsers, you can use other
protocols in a URL, such as file transfer (FTP), email (mailto), database
access (JDBC), and others platform-specific protocols. On some platforms, you
can use `OpenURL` to do different types of tasks in Unity.  
  
The `OpenURL` command is powerful and on some platforms, it can even open
local files, run commands, and open connections over any protocol that the
platform and security sandbox supports.  
  
The `OpenURL` method runs with the same permissions as your app itself. For
example, if your app is running as a WebGL player in a desktop web browser, it
cannot access local files on the machine, because the WebGL platform runs
inside a security sandbox which prevents that. However, this method is more
powerful on platforms such as a desktop platform exe app, where it runs with
fewer security restrictions without a security sandbox.  
  
**Important:** Be cautious and do NOT pass a string to the OpenURL function to
prevent any malicious attempts from third-party software.  
  
On desktop platforms, you should consider this method to have similar security
implications as an [eval](https://en.wikipedia.org/wiki/Eval) type function,
which is present in most programming languages.  
  
If your app uses OpenURL to open URL strings from a third-party, or the
strings put together using any user-supplied data, then that data should be
considered untrusted and used to run arbitrary code under the same permissions
of your app. You must also sanitise the untrusted data and validate to ensure
that it generates the expected input for your application.  
  
**WebGL:** From version 2019.4.25f1, 2020.3.5f1, 2021.1.2f1, and 2021.2.0a11,
`Application.OpenURL` opens the URL in a new browser tab. In previous
versions,`Application.OpenURL` opens the URL in the same browser tab, which
terminates the active Unity application. To customize this behavior for any
version, implement your own open URL function with a custom .jslib and C#
method instead of using `Application.OpenURL`. Refer to [Interaction with
browser scripting](../Manual/webgl-interactingwithbrowserscripting.html) for
more information and examples.  
  
**Android:** Due to security changes in Android 7.0 ([More
information](https://developer.android.com/about/versions/nougat/android-7.0-changes#sharing-
files)), `Application.OpenURL` can no longer be used for opening local app
files. To share files with other applications, you must use
([FileProvider](https://developer.android.com/reference/androidx/core/content/FileProvider)).  
  
**iOS:** `Application.OpenURL` cannot be used for opening local files.  
  
_Example:_

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Application.OpenURL](Application.OpenURL.html)("http://unity3d.com/");
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

