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

#  [EditorGUI](EditorGUI.html).Vector4Field

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

public static [Vector4](Vector4.html) Vector4Field([Rect](Rect.html) position,
string label, [Vector4](Vector4.html) value);

### Parameters

position | Rectangle on the screen to use for the field.  
---|---  
label | Label to display above the field.  
value | The value to edit.  
  
### Returns

**Vector4** The value entered by the user.

### Description

Makes an X, Y, Z, and W field for entering a [Vector4](Vector4.html).

![](../StaticFiles/ScriptRefImages/EditorGUIVector4Field.png)  
_Vector4 field in an Editor Window._

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // [Editor](Editor.html) window that shows the detailed rotation (X,Y,Z and W components),
    // the position in 3D space and position in [Screen](Screen.html) space of the selected
    // transform.  
      
    class CustomTransformInspector : [EditorWindow](EditorWindow.html)
    {
        bool showing = true;
        [Vector4](Vector4.html) rotationComp;  
      
        [[MenuItem](MenuItem.html)("Examples/[GameObject](GameObject.html) detailed inspector")]
        static void Init()
        {
            CustomTransformInspector window = (CustomTransformInspector)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(CustomTransformInspector));
            window.Show();
        }  
      
        void OnInspectorUpdate()
        {
            Repaint();
        }  
      
        void OnGUI()
        {
            var currObj = [Selection.activeTransform](Selection-activeTransform.html);  
      
            showing = [EditorGUI.InspectorTitlebar](EditorGUI.InspectorTitlebar.html)(new [Rect](Rect.html)(0, 0, position.width, 20), showing, currObj, showing);
            if (showing)
            {
                if (currObj)
                {
                    currObj.position = [EditorGUI.Vector3Field](EditorGUI.Vector3Field.html)(new [Rect](Rect.html)(3, 15, position.width - 6, 20),
                        "[Position](UIElements.Position.html) in 3D [Space](Space.html):",
                        currObj.position);  
      
                    [EditorGUI.Vector2Field](EditorGUI.Vector2Field.html)(new [Rect](Rect.html)(3, 50, position.width - 6, 20),
                        "[Position](UIElements.Position.html) in [Screen](Screen.html) [Space](Space.html):",
                        Camera.main.WorldToScreenPoint(currObj.position));  
      
                    rotationComp = [EditorGUI.Vector4Field](EditorGUI.Vector4Field.html)(new [Rect](Rect.html)(3, 85, position.width - 6, 20),
                        "Detailed Rotation:",
                        QuaternionToVector4(currObj.localRotation));
                    currObj.localRotation = ConvertToQuaternion(rotationComp);  
      
                    currObj.localScale = [EditorGUI.Vector3Field](EditorGUI.Vector3Field.html)(new [Rect](Rect.html)(3, 120, position.width - 6, 20),
                        "[Scale](UIElements.Scale.html):",
                        currObj.localScale);
                }
                else
                {
                    [EditorGUI.DropShadowLabel](EditorGUI.DropShadowLabel.html)(
                        new [Rect](Rect.html)(3, 15, position.width, 20),
                        "Select an Object to inspect");
                }
            }
        }  
      
        [Quaternion](Quaternion.html) ConvertToQuaternion([Vector4](Vector4.html) v4)
        {
            return new [Quaternion](Quaternion.html)(v4.x, v4.y, v4.z, v4.w);
        }  
      
        [Vector4](Vector4.html) QuaternionToVector4([Quaternion](Quaternion.html) q)
        {
            return new [Vector4](Vector4.html)(q.x, q.y, q.z, q.w);
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

