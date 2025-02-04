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

#  [GUILayout](GUILayout.html).FlexibleSpace

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

public static void FlexibleSpace();

### Description

Insert a flexible space element.

Flexible spaces use up any leftover space in a layout.  
  
**Note:** This will override the
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html) and
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html)  
  
![](../StaticFiles/ScriptRefImages/GUILayoutFlexibleSpace.png)  
_Flexible Space in a GUILayout Area._

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        float sliderValue = 1.0f;  
      
        void OnGUI()
        {
            // [Wrap](UIElements.Wrap.html) everything in the designated [GUI](GUI.html) Area
            [GUILayout.BeginArea](GUILayout.BeginArea.html)(new [Rect](Rect.html)(0, 0, 200, 60));
            // Begin the singular Horizontal [Group](Experimental.GraphView.Group.html)
            [GUILayout.BeginHorizontal](GUILayout.BeginHorizontal.html)();
            // Place a [Button](UIElements.Button.html) normally
            [GUILayout.RepeatButton](GUILayout.RepeatButton.html)("A button with\ntwo lines");
            // Place a space between the button and the vertical area
            // so it fits the whole area
            [GUILayout.FlexibleSpace](GUILayout.FlexibleSpace.html)();
            // Arrange two more Controls vertically beside the [Button](UIElements.Button.html)
            [GUILayout.BeginVertical](GUILayout.BeginVertical.html)();
            [GUILayout.Box](GUILayout.Box.html)("Value:" + [Mathf.Round](Mathf.Round.html)(sliderValue));
            sliderValue = [GUILayout.HorizontalSlider](GUILayout.HorizontalSlider.html)(sliderValue, 0.0f, 10f);  
      
            // End the Groups and Area
            [GUILayout.EndVertical](GUILayout.EndVertical.html)();
            [GUILayout.EndHorizontal](GUILayout.EndHorizontal.html)();
            [GUILayout.EndArea](GUILayout.EndArea.html)();
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

