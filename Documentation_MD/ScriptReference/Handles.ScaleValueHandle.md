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

#  [Handles](Handles.html).ScaleValueHandle

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

public static float ScaleValueHandle(float value, [Vector3](Vector3.html)
position, [Quaternion](Quaternion.html) rotation, float size,
[Handles.CapFunction](Handles.CapFunction.html) capFunction, float snap);

### Parameters

value | The value the user can modify.  
---|---  
position | The position of the handle in the space of [Handles.matrix](Handles-matrix.html).  
rotation | The rotation of the handle in the space of [Handles.matrix](Handles-matrix.html).  
size | The size of the handle in the space of [Handles.matrix](Handles-matrix.html). Use [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html) if you want a constant screen-space size.  
snap | The snap increment. See [Handles.SnapValue](Handles.SnapValue.html).  
capFunction | The function to call for doing the actual drawing.  
  
### Returns

**float** The new value modified by the user's interaction with the handle. If
the user has not moved the handle, it will return the same value as you passed
into the function.

### Description

Make a 3D handle that scales a single float.

This method will draw a 3D-draggable handle on the screen. The handle does not
move and will scale a single float up and down.  
  
![](../StaticFiles/ScriptRefImages/ScaleValueHandle.png)  
_Scale Value handle in the Scene view with an arrow cap as the handle._  
  
Add the following script to your Assets folder as LightColorLerp.cs and add
the LightColorLerp component to an object in a Scene.

    
    
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html), [RequireComponent](RequireComponent.html)(typeof([Light](Light.html)))]
    public class LightColorLerp : [MonoBehaviour](MonoBehaviour.html)
    {
        [[SerializeField](SerializeField.html)]
        private [Color](Color.html) m_Color1 = [Color.red](Color-red.html);
        [[SerializeField](SerializeField.html)]
        private [Color](Color.html) m_Color2 = [Color.green](Color-green.html);  
      
        public float amount { get { return m_Amount; } set { m_Amount = [Mathf.Clamp01](Mathf.Clamp01.html)(value); } }
        [[SerializeField](SerializeField.html), Range(0f, 1f)]
        private float m_Amount = 1f;  
      
        private [Light](Light.html) m_Light;  
      
        protected virtual void OnEnable()
        {
            m_Light = GetComponent<[Light](Light.html)>();
        }  
      
        public virtual void [Update](PlayerLoop.Update.html)()
        {
            m_Light.color = [Color.Lerp](Color.Lerp.html)(m_Color1, m_Color2, m_Amount);
        }
    }
    

Add the following script to Assets/Editor as LightColorLerpEditor.cs and
select the object with the LightColorLerp component.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(LightColorLerp)), [CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class LightColorLerpEditor : [Editor](Editor.html)
    {
        protected virtual void OnSceneGUI()
        {
            LightColorLerp colorLerp = (LightColorLerp)target;  
      
            float size = [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html)(colorLerp.transform.position) * 5f;
            float snap = 0.1f;  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            float newAmount = [Handles.ScaleValueHandle](Handles.ScaleValueHandle.html)(colorLerp.amount, colorLerp.transform.position, [Quaternion.identity](Quaternion-identity.html), size, [Handles.ArrowHandleCap](Handles.ArrowHandleCap.html), snap);
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                [Undo.RecordObject](Undo.RecordObject.html)(colorLerp, "Change [Light](Light.html) [Color](Color.html) Interpolation");
                colorLerp.amount = newAmount;
                colorLerp.Update();
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

