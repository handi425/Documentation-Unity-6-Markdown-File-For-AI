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

# ApplicationTitleDescriptor

class in UnityEditor

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

### Description

Utility class containing all the information necessary to format Unity Editor
main window title. All the various fields are concatenated to create a fully
formed title. If only
[ApplicationTitleDescriptor.title](ApplicationTitleDescriptor-title.html) is
provided, this will become the complete title.

See also: [EditorApplication.updateMainWindowTitle](EditorApplication-
updateMainWindowTitle.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    
    public class WindowTitleExample
    {
        private static void CustomTitleBar([ApplicationTitleDescriptor](ApplicationTitleDescriptor.html) desc)
        {
            desc.title = $"My [Editor](Editor.html) Custom Title version: {[Random.value](Random-value.html)}";
        }
    
        [[MenuItem](MenuItem.html)("Test/Setup custom title bar")]
        static void Setup()
        {
            [EditorApplication.updateMainWindowTitle](EditorApplication-updateMainWindowTitle.html) -= CustomTitleBar;
            // This callback will be triggered when a new scene is loaded or when Unity starts.
            [EditorApplication.updateMainWindowTitle](EditorApplication-updateMainWindowTitle.html) += CustomTitleBar;
            [EditorApplication.UpdateMainWindowTitle](EditorApplication.UpdateMainWindowTitle.html)();
        }
    }
    

### Properties

[activeSceneName](ApplicationTitleDescriptor-activeSceneName.html)| Unity
active scene.  
---|---  
[codeCoverageEnabled](ApplicationTitleDescriptor-codeCoverageEnabled.html)| Is
code coverage enabled.  
[projectName](ApplicationTitleDescriptor-projectName.html)| Current project
name.  
[targetName](ApplicationTitleDescriptor-targetName.html)| What is the runtime
target for a Unity build.  
[title](ApplicationTitleDescriptor-title.html)| Setting this field will set
the complete editor title without using any of the other fields of
ApplicationTitleDescriptor.  
[unityProductName](ApplicationTitleDescriptor-unityProductName.html)| Unity
version name in the form of: Unity <number> <release stream (optional)>.  
[unityVersion](ApplicationTitleDescriptor-unityVersion.html)| Unity version
number.  
  
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

