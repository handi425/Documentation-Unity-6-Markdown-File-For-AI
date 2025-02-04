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

# DisabledScope

struct in UnityEditor

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

Create a group of controls that can be disabled.

If disabled is true, the controls inside the group will be disabled. If false,
the enabled/disabled state will not be changed.  
  
The group cannot be used to enable controls that would otherwise be disabled
to begin with. The groups can be nested and the controls within a child group
will be disabled either if that child group is itself disabled or if a parent
group is.

    
    
    using [UnityEditor](UnityEditor.html);  
      
    class ExampleClass
    {
        bool canJump = false;
        float jumpHeight = 0f;  
      
        void Example()
        {
            canJump = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("Can Jump", canJump);  
      
            // Disable the jumping height control if canJump is false:
            using (new [EditorGUI.DisabledScope](EditorGUI.DisabledScope.html)(canJump == false))
            {
                jumpHeight = [EditorGUILayout.FloatField](EditorGUILayout.FloatField.html)("Jump Height", jumpHeight);
            }
        }
    }
    

### Constructors

[EditorGUI.DisabledScope](EditorGUI.DisabledScope-ctor.html)| Create a new
DisabledScope and begin the corresponding group.  
---|---  
  
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

