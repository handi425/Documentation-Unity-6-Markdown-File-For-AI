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

#  [EditorGUI](EditorGUI.html).LabelField

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

public static void LabelField([Rect](Rect.html) position, string label,
[GUIStyle](GUIStyle.html) style = EditorStyles.label);

## Declaration

public static void LabelField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, [GUIStyle](GUIStyle.html) style =
EditorStyles.label);

## Declaration

public static void LabelField([Rect](Rect.html) position, string label, string
label2, [GUIStyle](GUIStyle.html) style = EditorStyles.label);

## Declaration

public static void LabelField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, [GUIContent](GUIContent.html) label2,
[GUIStyle](GUIStyle.html) style = EditorStyles.label);

### Parameters

position | Rectangle on the screen to use for the label field.  
---|---  
label | Label in front of the label field.  
label2 | The label to show to the right.  
style | Style information (color, etc) for displaying the label.  
  
### Description

Makes a label field. (Useful for showing read-only info.)

![](../StaticFiles/ScriptRefImages/EditorGUILabelField.png)  
_Shows a label in an editor window with the seconds since the editor started._

    
    
    // Shows a label in the editor with the seconds since the editor started  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;  
      
    //Select the dependencies of the found [GameObject](GameObject.html)
    public class EditorGUIObjectField : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/[EditorGUI](EditorGUI.html) [Label](UIElements.Label.html) Usage")]
        static void Init()
        {
            UnityEditor.EditorWindow window = GetWindow(typeof(EditorGUIObjectField));
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(3, 3, position.width, 20),
                "[Time](Time.html) since start: ",
                EditorApplication.timeSinceStartup.ToString());
            this.Repaint();
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

