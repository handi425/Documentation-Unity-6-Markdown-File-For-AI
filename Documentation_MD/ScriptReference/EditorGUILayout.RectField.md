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

#  [EditorGUILayout](EditorGUILayout.html).RectField

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

public static [Rect](Rect.html) RectField([Rect](Rect.html) value, params
GUILayoutOption[] options);

## Declaration

public static [Rect](Rect.html) RectField(string label, [Rect](Rect.html)
value, params GUILayoutOption[] options);

## Declaration

public static [Rect](Rect.html) RectField([GUIContent](GUIContent.html) label,
[Rect](Rect.html) value, params GUILayoutOption[] options);

### Parameters

label | Label to display above the field.  
---|---  
value | The value to edit.  
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

**Rect** The value entered by the user.

### Description

Make an X, Y, W & H field for entering a [Rect](Rect.html).

![](../StaticFiles/ScriptRefImages/MoveResizeSelectedWindow2.png)  
_Capture the RectField sizes._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class RectFieldExample : [EditorWindow](EditorWindow.html)
    {
        static [Rect](Rect.html) pos;  
      
        [[MenuItem](MenuItem.html)("Examples/[RectField](UIElements.RectField.html) Example")]
        static void rectFieldExample()
        {
            RectFieldExample window =
                [EditorWindow.GetWindowWithRect](EditorWindow.GetWindowWithRect.html)<RectFieldExample>(new [Rect](Rect.html)(0, 0, 250, 100));
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUILayout.BeginVertical](EditorGUILayout.BeginVertical.html)();
            pos =  [EditorGUILayout.RectField](EditorGUILayout.RectField.html)("Internal input:", pos);  
      
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();
            [GUILayout.FlexibleSpace](GUILayout.FlexibleSpace.html)();
            [GUILayout.Label](GUILayout.Label.html)("x: " + (pos.x).ToString());
            [GUILayout.FlexibleSpace](GUILayout.FlexibleSpace.html)();
            [GUILayout.Label](GUILayout.Label.html)("y: " + (pos.y).ToString());
            [GUILayout.FlexibleSpace](GUILayout.FlexibleSpace.html)();
            [GUILayout.Label](GUILayout.Label.html)("w: " + (pos.width).ToString());
            [GUILayout.FlexibleSpace](GUILayout.FlexibleSpace.html)();
            [GUILayout.Label](GUILayout.Label.html)("h: " + (pos.height).ToString());
            [GUILayout.FlexibleSpace](GUILayout.FlexibleSpace.html)();
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();
            [EditorGUILayout.EndVertical](EditorGUILayout.EndVertical.html)();  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Close"))
            {
                this.Close();
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

