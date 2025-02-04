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

#  [EditorApplication](EditorApplication.html).applicationPath

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

public static string applicationPath;

### Description

Gets the path to the Unity Editor application. (Read Only)

The path to the Unity Editor can vary depending on your configuration. If you
installed the 2021.3 Editor from the Hub on Windows, you might have a path
like this: `C:/Program Files/Unity/Hub/Editor/2021.3.10f1/Editor/Unity.exe`.
Additional resources: [applicationContentsPath](EditorApplication-
applicationContentsPath.html).

    
    
    // [Display](Display.html) file system location where the Unity
    // executable is stored.  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class ApplicationPathExample
    {
        // Create a menu item called "[Location](FilePathAttribute.Location.html) of Unity application" in the "Examples" [Menu](Menu.html). 
        // In the [Editor](Editor.html), click on "[Location](FilePathAttribute.Location.html) of Unity [Application](Application.html)" in the menu to display the path to the Unity executable in the Console.
        [[MenuItem](MenuItem.html)("Examples/[Location](FilePathAttribute.Location.html) of Unity application")]
        static void AppPath()
        {
            [Debug.Log](Debug.Log.html)([EditorApplication.applicationPath](EditorApplication-applicationPath.html));
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

