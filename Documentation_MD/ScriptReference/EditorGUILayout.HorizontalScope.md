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

# HorizontalScope

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

Disposable helper class for managing
[BeginHorizontal](EditorGUILayout.BeginHorizontal.html) /
[EndHorizontal](EditorGUILayout.EndHorizontal.html).

This is an extension to
[GUILayout.HorizontalScope](GUILayout.HorizontalScope.html). It can be used
for making compound controls  
  
![](../StaticFiles/ScriptRefImages/BeginEndHorizontalExample.png)  
_Horizontal Compound group._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // Create a Horizontal Compound [Button](UIElements.Button.html)
    class HorizontalScopeExample : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/Horizontal scope usage")]
        static void Init()
        {
            var window = GetWindow<HorizontalScopeExample>();
            window.Show();
        }  
      
        void OnGUI()
        {
            using (var h = new [EditorGUILayout.HorizontalScope](EditorGUILayout.HorizontalScope.html)("[Button](UIElements.Button.html)"))
            {
                if ([GUI.Button](GUI.Button.html)(h.rect, [GUIContent.none](GUIContent-none.html)))
                    [Debug.Log](Debug.Log.html)("Go here");
                [GUILayout.Label](GUILayout.Label.html)("I'm inside the button");
                [GUILayout.Label](GUILayout.Label.html)("So am I");
            }
        }
    }
    

### Properties

[rect](EditorGUILayout.HorizontalScope-rect.html)| The rect of the horizontal
group.  
---|---  
  
### Constructors

[EditorGUILayout.HorizontalScope](EditorGUILayout.HorizontalScope-ctor.html)|
Create a new HorizontalScope and begin the corresponding horizontal group.  
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

