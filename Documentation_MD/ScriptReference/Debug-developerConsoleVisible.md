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

#  [Debug](Debug.html).developerConsoleVisible

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

[Switch to Manual](../Manual/class-Debug.html "Go to Debug Component in the
Manual")

public static bool developerConsoleVisible;

### Description

Controls whether the development console is visible.

The developer console is a window that can appear when a development build of
your project is running. It is similar to the Console window in the Editor,
but appears at runtime. The development console automatically appears when an
error has been logged, and [Debug.developerConsoleEnabled](Debug-
developerConsoleEnabled.html) is true. For example:

    
    
    using UnityEngine;  
      
    public class LogErrorScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Debug.LogError](Debug.LogError.html)("I am an [Error](PackageManager.Error.html)");
        }
    }
    

You can close the development console when opened by using:

    
    
    using UnityEngine;  
      
    public class CloseDevConsoleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Debug.developerConsoleVisible](Debug-developerConsoleVisible.html) = false;
        }
    }
    

You can reopen the development console if at least one entry exists in the
console by using:

    
    
    using UnityEngine;  
      
    public class OpenDevConsoleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Debug.developerConsoleVisible](Debug-developerConsoleVisible.html) = true;
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

