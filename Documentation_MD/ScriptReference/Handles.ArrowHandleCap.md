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

#  [Handles](Handles.html).ArrowHandleCap

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

public static void ArrowHandleCap(int controlID, [Vector3](Vector3.html)
position, [Quaternion](Quaternion.html) rotation, float size,
[EventType](EventType.html) eventType);

### Parameters

controlID | The control ID for the handle.  
---|---  
position | The position of the handle in the space of [Handles.matrix](Handles-matrix.html).  
rotation | The rotation of the handle in the space of [Handles.matrix](Handles-matrix.html).  
size | The size of the handle in the space of [Handles.matrix](Handles-matrix.html). Use [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html) if you want a constant screen-space size.  
eventType | Event type for the handle to act upon. By design it handles [EventType.Layout](EventType.Layout.html) and [EventType.Repaint](EventType.Repaint.html) events.  
  
### Description

Draw an arrow like those used by the move tool.

On [EventType.Layout](EventType.Layout.html) event, calculates handle distance
to mouse and calls [HandleUtility.AddControl](HandleUtility.AddControl.html)
accordingly.  
  
On [EventType.Repaint](EventType.Repaint.html) event, draws the handle shape.  
  
![](../StaticFiles/ScriptRefImages/ArrowCap.png) _Arrow Handle Cap in the
Scene View._  
  
Add the following script to your Assets folder as ArrowExample.cs and add the
ArrowExample component to an object in a Scene.

    
    
    using UnityEngine;  
      
    public class ArrowExample : [MonoBehaviour](MonoBehaviour.html) {}
    

Add the following script to Assets/Editor as ArrowExampleEditor.cs and select
the object with the ArrowExample component.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(ArrowExample))]
    public class ArrowExampleEditor : [Editor](Editor.html)
    {
        float size = 1f;  
      
        protected virtual void OnSceneGUI()
        {
            if (Event.current.type == [EventType.Repaint](EventType.Repaint.html))
            {
                [Transform](Transform.html) transform = ((ArrowExample)target).transform;
                [Handles.color](Handles-color.html) = [Handles.xAxisColor](Handles-xAxisColor.html);
                [Handles.ArrowHandleCap](Handles.ArrowHandleCap.html)(
                    0,
                    transform.position + new [Vector3](Vector3.html)(3f, 0f, 0f),
                    transform.rotation * [Quaternion.LookRotation](Quaternion.LookRotation.html)([Vector3.right](Vector3-right.html)),
                    size,
                    [EventType.Repaint](EventType.Repaint.html)
                );
                [Handles.color](Handles-color.html) = [Handles.yAxisColor](Handles-yAxisColor.html);
                [Handles.ArrowHandleCap](Handles.ArrowHandleCap.html)(
                    0,
                    transform.position + new [Vector3](Vector3.html)(0f, 3f, 0f),
                    transform.rotation * [Quaternion.LookRotation](Quaternion.LookRotation.html)([Vector3.up](Vector3-up.html)),
                    size,
                    [EventType.Repaint](EventType.Repaint.html)
                );
                [Handles.color](Handles-color.html) = [Handles.zAxisColor](Handles-zAxisColor.html);
                [Handles.ArrowHandleCap](Handles.ArrowHandleCap.html)(
                    0,
                    transform.position + new [Vector3](Vector3.html)(0f, 0f, 3f),
                    transform.rotation * [Quaternion.LookRotation](Quaternion.LookRotation.html)([Vector3.forward](Vector3-forward.html)),
                    size,
                    [EventType.Repaint](EventType.Repaint.html)
                );
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

