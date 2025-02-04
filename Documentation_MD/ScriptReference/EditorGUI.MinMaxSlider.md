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

#  [EditorGUI](EditorGUI.html).MinMaxSlider

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

**Obsolete** Switch the order of the first two parameters.

## Declaration

public static void MinMaxSlider([GUIContent](GUIContent.html) label,
[Rect](Rect.html) position, ref float minValue, ref float maxValue, float
minLimit, float maxLimit);

## Declaration

public static void MinMaxSlider([Rect](Rect.html) position, ref float
minValue, ref float maxValue, float minLimit, float maxLimit);

## Declaration

public static void MinMaxSlider([Rect](Rect.html) position, string label, ref
float minValue, ref float maxValue, float minLimit, float maxLimit);

## Declaration

public static void MinMaxSlider([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, ref float minValue, ref float maxValue,
float minLimit, float maxLimit);

### Parameters

position | Rectangle on the screen to use for the slider.  
---|---  
label | Optional label in front of the slider.  
minValue | The lower value of the range the slider shows, passed by reference.  
maxValue | The upper value at the range the slider shows, passed by reference.  
minLimit | The limit at the left end of the slider.  
maxLimit | The limit at the right end of the slider.  
  
### Description

Makes a special slider the user can use to specify a range between a min and a
max.

![](../StaticFiles/ScriptRefImages/EditorGUIMinMaxSlider.png)  
_MinMax Slider in an Editor Window._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    
    // Place the selected object randomly between the interval of the Min Max [Slider](UIElements.Slider.html)
    // in the X,Y,Z coords  
      
    class EditorGUIMinMaxSlider : [EditorWindow](EditorWindow.html)
    {
        float minVal = -10;
        float minLimit = -20;
        float maxVal = 10;
        float maxLimit = 20;  
      
        [[MenuItem](MenuItem.html)("Examples/[Editor](Editor.html) [GUI](GUI.html) Move Object Randomly")]
        static void Init()
        {
            var window = GetWindow<EditorGUIMinMaxSlider>();
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUI.MinMaxSlider](EditorGUI.MinMaxSlider.html)(
                new [Rect](Rect.html)(0, 0, position.width, 20),
                new [GUIContent](GUIContent.html)("[Random](Random.html) range:"),
                ref minVal, ref maxVal,
                minLimit, maxLimit);
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 25, position.width, position.height - 25), "Randomize!"))
            {
                PlaceRandomly();
            }
        }  
      
        void PlaceRandomly()
        {
            if ([Selection.activeTransform](Selection-activeTransform.html))
            {
                Selection.activeTransform.position =
                    new [Vector3](Vector3.html)(
                        [Random.Range](Random.Range.html)(minVal, maxVal),
                        [Random.Range](Random.Range.html)(minVal, maxVal),
                        [Random.Range](Random.Range.html)(minVal, maxVal)
                    );
            }
            else
            {
                [Debug.LogError](Debug.LogError.html)("Select a [GameObject](GameObject.html) to randomize its position.");
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

