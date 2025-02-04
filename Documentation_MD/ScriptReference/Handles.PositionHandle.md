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

#  [Handles](Handles.html).PositionHandle

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

public static [Vector3](Vector3.html) PositionHandle([Vector3](Vector3.html)
position, [Quaternion](Quaternion.html) rotation);

## Declaration

public static [Vector3](Vector3.html)
PositionHandle([Handles.PositionHandleIds](Handles.PositionHandleIds.html)
ids, [Vector3](Vector3.html) position, [Quaternion](Quaternion.html)
rotation);

### Parameters

position | The center of the handle in 3D space.  
---|---  
rotation | The orientation of the handle in 3D space.  
ids | The control IDs of the handles. Use PositionHandleIds.default.  
  
### Returns

**Vector3** The new value modified by the user's interaction with the handle.
If the user has not moved the handle, it will return the same value as you
passed into the function.

### Description

Make a position handle.

This handle behaves like the built-in move tool in Unity.  
  
![](../StaticFiles/ScriptRefImages/PositionHandle.png)  
Position handle in the Scene View.''  
  
Add the following script to your Assets folder as PositionHandleExample.cs and
add the PositionHandleExample component to an object in a Scene.

    
    
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class PositionHandleExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector3](Vector3.html) targetPosition { get { return m_TargetPosition; } set { m_TargetPosition = value; } }
        [[SerializeField](SerializeField.html)]
        private [Vector3](Vector3.html) m_TargetPosition = new [Vector3](Vector3.html)(1f, 0f, 2f);  
      
        public virtual void [Update](PlayerLoop.Update.html)()
        {
            transform.LookAt(m_TargetPosition);
        }
    }
    

Add the following script to Assets/Editor as PositionHandleExampleEditor.cs
and select the object with the PositionHandleExample component.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(PositionHandleExample)), [CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class PositionHandleExampleEditor : [Editor](Editor.html)
    {
        protected virtual void OnSceneGUI()
        {
            PositionHandleExample example = (PositionHandleExample)target;  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            [Vector3](Vector3.html) newTargetPosition = [Handles.PositionHandle](Handles.PositionHandle.html)(example.targetPosition, [Quaternion.identity](Quaternion-identity.html));
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                [Undo.RecordObject](Undo.RecordObject.html)(example, "Change Look At [Target](GraphicsBuffer.Target.html) [Position](UIElements.Position.html)");
                example.targetPosition = newTargetPosition;
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

