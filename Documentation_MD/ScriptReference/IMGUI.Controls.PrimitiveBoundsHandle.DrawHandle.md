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

#
[PrimitiveBoundsHandle](IMGUI.Controls.PrimitiveBoundsHandle.html).DrawHandle

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

public void DrawHandle();

### Description

A function to display this instance in the current handle camera using its
current configuration.

Always write properties to the handle before calling this function. Place the
calls to this function inside
[EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html) and
[EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html) to detect user
interaction and read the updated properties from the handle.  
  
The following component defines an object with a [Bounds](Bounds.html)
property.

    
    
    using UnityEngine;  
      
    public class BoundsExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Bounds](Bounds.html) bounds { get { return m_Bounds; } set { m_Bounds = value; } }
        [[SerializeField](SerializeField.html)]
        private [Bounds](Bounds.html) m_Bounds = new [Bounds](Bounds.html)([Vector3.zero](Vector3-zero.html), [Vector3.one](Vector3-one.html));
    }
    

The following Custom Editor allows the user to edit the bounds property for
this component in the Scene view.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.IMGUI.Controls;
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(BoundsExample)), [CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class BoundsExampleEditor : [Editor](Editor.html)
    {
        private [BoxBoundsHandle](IMGUI.Controls.BoxBoundsHandle.html) m_BoundsHandle = new [BoxBoundsHandle](IMGUI.Controls.BoxBoundsHandle.html)();  
      
        // the OnSceneGUI callback uses the [Scene](SceneManagement.Scene.html) view camera for drawing handles by default
        protected virtual void OnSceneGUI()
        {
            BoundsExample boundsExample = (BoundsExample)target;  
      
            // copy the target object's data to the handle
            m_BoundsHandle.center = boundsExample.bounds.center;
            m_BoundsHandle.size = boundsExample.bounds.size;  
      
            // draw the handle
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            m_BoundsHandle.DrawHandle();
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                // record the target object before setting new values so changes can be undone/redone
                [Undo.RecordObject](Undo.RecordObject.html)(boundsExample, "Change [Bounds](Bounds.html)");  
      
                // copy the handle's updated data back to the target object
                [Bounds](Bounds.html) newBounds = new [Bounds](Bounds.html)();
                newBounds.center = m_BoundsHandle.center;
                newBounds.size = m_BoundsHandle.size;
                boundsExample.bounds = newBounds;
            }
        }
    }
    

Additional resources: [Editor.OnSceneGUI](Editor.OnSceneGUI.html),
[Handles.SetCamera](Handles.SetCamera.html).

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

