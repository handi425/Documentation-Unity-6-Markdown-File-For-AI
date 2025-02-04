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

#  [GUIStyle](GUIStyle.html).CalcSize

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

[Switch to Manual](../Manual/class-GUIStyle.html "Go to GUIStyle Component in
the Manual")

## Declaration

public [Vector2](Vector2.html) CalcSize([GUIContent](GUIContent.html)
content);

### Description

Calculate the size of some content if it is rendered with this style.

This function does not take word wrapping into account. To do that, you need
to determine the allocated width and then call
[CalcHeight](GUIStyle.CalcHeight.html) to figure out the word wrapped height.

    
    
    // Example for the [GUIStyle.CalcSize](GUIStyle.CalcSize.html)  
      
    using UnityEngine;  
      
    public class CalcSizeExample : [MonoBehaviour](MonoBehaviour.html)
    {
        string s;  
      
        void Start()
        {
            s = "A string for [GUIContent](GUIContent.html)()";
        }  
      
        void OnGUI()
        {
            [GUIContent](GUIContent.html) content = new [GUIContent](GUIContent.html)(s);  
      
            [GUIStyle](GUIStyle.html) style = GUI.skin.box;
            style.alignment = [TextAnchor.MiddleCenter](TextAnchor.MiddleCenter.html);  
      
            // Compute how large the button needs to be.
            [Vector2](Vector2.html) size = style.CalcSize(content);  
      
            // make the [Box](UIElements.Box.html) double sized
            [GUI.Box](GUI.Box.html)(new [Rect](Rect.html)(10.0f, 10.0f, 2.0f * size.x, 2.0f * size.y), s);
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

