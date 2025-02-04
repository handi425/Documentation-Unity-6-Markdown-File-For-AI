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

#  [Handles](Handles.html).ScaleSlider

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

public static float ScaleSlider(float scale, [Vector3](Vector3.html) position,
[Vector3](Vector3.html) direction, [Quaternion](Quaternion.html) rotation,
float size, float snap);

## Declaration

public static float ScaleSlider(int id, float scale, [Vector3](Vector3.html)
position, [Vector3](Vector3.html) direction, [Quaternion](Quaternion.html)
rotation, float size, float snap);

### Parameters

scale | The value the user can modify.  
---|---  
position | The position of the handle in the space of [Handles.matrix](Handles-matrix.html).  
direction | The direction of the handle in the space of [Handles.matrix](Handles-matrix.html).  
rotation | The rotation of the handle in the space of [Handles.matrix](Handles-matrix.html).  
size | The size of the handle in the space of [Handles.matrix](Handles-matrix.html). Use [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html) if you want a constant screen-space size.  
snap | The snap increment. See [Handles.SnapValue](Handles.SnapValue.html).  
id | The control ID of the handle.  
  
### Returns

**float** The new value modified by the user's interaction with the handle. If
the user has not moved the handle, it will return the same value as you passed
into the function.

### Description

Make a directional scale slider.

This method will draw a 3D-draggable handle on the screen that looks like one
axis on Unity's built-in scale tool. The handle will stretch and will scale a
single float up and down.  
  
![](../StaticFiles/ScriptRefImages/ScaleSliderHandle.png)  
_Scale slider handle in the Scene View._  
  
Add the following script to your Assets folder as ScaleSliderExample.cs and
add the ScaleSliderExample component to an object in a Scene.

    
    
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class ScaleSliderExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public float scale { get { return m_Scale; } set { m_Scale = value; } }
        [[SerializeField](SerializeField.html)]
        private float m_Scale = 1f;  
      
        public virtual void [Update](PlayerLoop.Update.html)()
        {
            transform.localScale = new [Vector3](Vector3.html)(scale, 1f, 1f);
        }
    }
    

Add the following script to Assets/Editor as ScaleSliderExampleEditor.cs and
select the object with the ScaleSliderExample component.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(ScaleSliderExample)), [CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class ScaleSliderExampleEditor : [Editor](Editor.html)
    {
        public void OnSceneGUI()
        {
            ScaleSliderExample example = (ScaleSliderExample)target;  
      
            float size = [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html)(example.transform.position) * 1f;
            float snap = 0.5f;  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            float scale = [Handles.ScaleSlider](Handles.ScaleSlider.html)(example.scale, example.transform.position, example.transform.right, example.transform.rotation, size, snap);
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                [Undo.RecordObject](Undo.RecordObject.html)(target, "Change [Scale](UIElements.Scale.html) Value");
                example.scale = scale;
                example.Update();
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

