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

#  [EditorGUILayout](EditorGUILayout.html).CurveField

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

public static [AnimationCurve](AnimationCurve.html)
CurveField([AnimationCurve](AnimationCurve.html) value, params
GUILayoutOption[] options);

## Declaration

public static [AnimationCurve](AnimationCurve.html) CurveField(string label,
[AnimationCurve](AnimationCurve.html) value, params GUILayoutOption[]
options);

## Declaration

public static [AnimationCurve](AnimationCurve.html)
CurveField([GUIContent](GUIContent.html) label,
[AnimationCurve](AnimationCurve.html) value, params GUILayoutOption[]
options);

## Declaration

public static [AnimationCurve](AnimationCurve.html)
CurveField([AnimationCurve](AnimationCurve.html) value, [Color](Color.html)
color, [Rect](Rect.html) ranges, params GUILayoutOption[] options);

## Declaration

public static [AnimationCurve](AnimationCurve.html) CurveField(string label,
[AnimationCurve](AnimationCurve.html) value, [Color](Color.html) color,
[Rect](Rect.html) ranges, params GUILayoutOption[] options);

## Declaration

public static [AnimationCurve](AnimationCurve.html)
CurveField([GUIContent](GUIContent.html) label,
[AnimationCurve](AnimationCurve.html) value, [Color](Color.html) color,
[Rect](Rect.html) ranges, params GUILayoutOption[] options);

### Parameters

label | Optional label to display in front of the field.  
---|---  
value | The curve to edit.  
color | The color to show the curve with.  
ranges | Optional rectangle that the curve is restrained within.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Returns

**AnimationCurve** The curve edited by the user.

### Description

Make a field for editing an [AnimationCurve](AnimationCurve.html).

![](../StaticFiles/ScriptRefImages/FollowCurve.png)  
_Create an animation on the different axis and assign it to a GameObject._

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class FollowCurve : [EditorWindow](EditorWindow.html)
    {
        [AnimationCurve](AnimationCurve.html) curveX = [AnimationCurve.Linear](AnimationCurve.Linear.html)(0, 0, 10, 10);
        [AnimationCurve](AnimationCurve.html) curveY = [AnimationCurve.Linear](AnimationCurve.Linear.html)(0, 0, 10, 10);
        [AnimationCurve](AnimationCurve.html) curveZ = [AnimationCurve.Linear](AnimationCurve.Linear.html)(0, 0, 10, 10);  
      
        [[MenuItem](MenuItem.html)("Examples/Create Curve For Object")]
        static void Init()
        {
            FollowCurve window = (FollowCurve)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(FollowCurve));
            window.Show();
        }  
      
        void OnGUI()
        {
            curveX = [EditorGUILayout.CurveField](EditorGUILayout.CurveField.html)("[Animation](Animation.html) on X", curveX);
            curveY = [EditorGUILayout.CurveField](EditorGUILayout.CurveField.html)("[Animation](Animation.html) on Y", curveY);
            curveZ = [EditorGUILayout.CurveField](EditorGUILayout.CurveField.html)("[Animation](Animation.html) on Z", curveZ);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Generate Curve"))
                AddCurveToSelectedGameObject();
        }  
      
        void  AddCurveToSelectedGameObject()
        {
            if ([Selection.activeGameObject](Selection-activeGameObject.html))
            {
                FollowAnimationCurve comp =
                    Selection.activeGameObject.AddComponent<FollowAnimationCurve>();  
      
                comp.SetCurves(curveX, curveY, curveZ);
            }
            else
            {
                [Debug.LogError](Debug.LogError.html)("No Game Object selected for adding an animation curve");
            }
        }
    }
    

And the script that works with the example:

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class FollowAnimationCurve : [MonoBehaviour](MonoBehaviour.html)
    {
        public [AnimationCurve](AnimationCurve.html) curveX;
        public [AnimationCurve](AnimationCurve.html) curveY;
        public [AnimationCurve](AnimationCurve.html) curveZ;  
      
        public void SetCurves([AnimationCurve](AnimationCurve.html) xC, [AnimationCurve](AnimationCurve.html) yC, [AnimationCurve](AnimationCurve.html) zC)
        {
            curveX = xC;
            curveY = yC;
            curveZ = zC;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            transform.position = new [Vector3](Vector3.html)(curveX.Evaluate([Time.time](Time-time.html)), curveY.Evaluate([Time.time](Time-time.html)), curveZ.Evaluate([Time.time](Time-time.html)));
        }
    }
    

* * *

## Declaration

public static void CurveField([SerializedProperty](SerializedProperty.html)
property, [Color](Color.html) color, [Rect](Rect.html) ranges, params
GUILayoutOption[] options);

## Declaration

public static void CurveField([SerializedProperty](SerializedProperty.html)
property, [Color](Color.html) color, [Rect](Rect.html) ranges,
[GUIContent](GUIContent.html) label, params GUILayoutOption[] options);

### Parameters

property | The curve to edit.  
---|---  
color | The color to show the curve with.  
ranges | Optional rectangle that the curve is restrained within.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
label | Optional label to display in front of the field. Pass [[GUIContent.none] to hide the label.  
  
### Description

Make a field for editing an [AnimationCurve](AnimationCurve.html).

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

