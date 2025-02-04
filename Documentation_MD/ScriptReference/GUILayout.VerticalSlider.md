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

#  [GUILayout](GUILayout.html).VerticalSlider

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

public static float VerticalSlider(float value, float leftValue, float
rightValue, params GUILayoutOption[] options);

## Declaration

public static float VerticalSlider(float value, float leftValue, float
rightValue, [GUIStyle](GUIStyle.html) slider, [GUIStyle](GUIStyle.html) thumb,
params GUILayoutOption[] options);

### Parameters

value | The value the slider shows. This determines the position of the draggable thumb.  
---|---  
topValue | The value at the top end of the slider.  
bottomValue | The value at the bottom end of the slider.  
slider | The [GUIStyle](GUIStyle.html) to use for displaying the dragging area. If left out, the `horizontalSlider` style from the current [GUISkin](GUISkin.html) is used.  
thumb | The [GUIStyle](GUIStyle.html) to use for displaying draggable thumb. If left out, the `horizontalSliderThumb` style from the current [GUISkin](GUISkin.html) is used.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.  
  
### Returns

**float** The value that has been set by the user.

### Description

A vertical slider the user can drag to change a value between a min and a max.

![](../StaticFiles/ScriptRefImages/GUILayoutVerticalSlider.png)  
_Vertical slider in the Game View._

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draws a vertical slider control that goes from  10 (top) to 0 (bottom)
        float vSliderValue = 0.0f;  
      
        void OnGUI()
        {
            vSliderValue = [GUILayout.VerticalSlider](GUILayout.VerticalSlider.html)(vSliderValue, 10.0f, 0.0f);
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

