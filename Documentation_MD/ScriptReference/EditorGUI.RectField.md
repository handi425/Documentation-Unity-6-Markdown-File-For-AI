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

#  [EditorGUI](EditorGUI.html).RectField

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

public static [Rect](Rect.html) RectField([Rect](Rect.html) position,
[Rect](Rect.html) value);

## Declaration

public static [Rect](Rect.html) RectField([Rect](Rect.html) position, string
label, [Rect](Rect.html) value);

## Declaration

public static [Rect](Rect.html) RectField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, [Rect](Rect.html) value);

### Parameters

position | Rectangle on the screen to use for the field.  
---|---  
label | Optional label to display above the field.  
value | The value to edit.  
  
### Returns

**Rect** The value entered by the user.

### Description

Makes an X, Y, W, and H field for entering a [Rect](Rect.html).

![](../StaticFiles/ScriptRefImages/EditorGUIRectField.png)  
_Rect field in an Editor Window._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // Find all the cameras in the [Scene](SceneManagement.Scene.html) and shows all their viewports togheter  
      
    class EditorGUIRectField : [EditorWindow](EditorWindow.html)
    {
        [Camera](Camera.html)[] cameras;  
      
        [[MenuItem](MenuItem.html)("Examples/[Editor](Editor.html) [GUI](GUI.html) [RectField](UIElements.RectField.html) usage")]
        static void Init()
        {
            var window = GetWindow<EditorGUIRectField>();
            window.position = new [Rect](Rect.html)(0, 0, 150, 120);
            window.Show();
        }  
      
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(3, 3, position.width - 6, 20), "[Update](PlayerLoop.Update.html) list"))
                cameras = FindObjectsOfType<[Camera](Camera.html)>();  
      
            if (cameras.Length > 0)
            {
                for (var i = 0; i < cameras.Length; i++)
                {
                    cameras[i].rect = [EditorGUI.RectField](EditorGUI.RectField.html)(
                        new [Rect](Rect.html)(3, 25 + 45 * i, position.width - 6, 25),
                        cameras[i].name,
                        cameras[i].rect);
                }
            }
        }
    }
    

* * *

### Description

Makes an X, Y, W, and H for Rect using SerializedProperty (not public).

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

