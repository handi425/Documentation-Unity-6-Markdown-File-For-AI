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

# JointAngularLimitHandle

class in UnityEditor.IMGUI.Controls

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

### Description

A class for a compound handle to edit multiaxial angular motion limits in the
Scene view.

![](../StaticFiles/ScriptRefImages/JointAngularLimitHandle.png)
_JointAngularLimitHandle in the Scene View._  
  
The shapes rendered by the
[DrawHandle](IMGUI.Controls.JointAngularLimitHandle.DrawHandle.html) method
assume that angular limits are applied first along the x-axis, then the
y-axis, and finally the z-axis.  
  
The following component defines angular limits for a
[CharacterJoint](CharacterJoint.html) to be added at run time.

    
    
    using UnityEngine;  
      
    public class JointExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public float xMin { get { return m_XMin; } set { m_XMin = value; } }
        [[SerializeField](SerializeField.html)]
        float m_XMin = -45f;  
      
        public float xMax { get { return m_XMax; } set { m_XMax = value; } }
        [[SerializeField](SerializeField.html)]
        float m_XMax = 45f;  
      
        public float yMax { get { return m_YMax; } set { m_YMax = value; } }
        [[SerializeField](SerializeField.html)]
        float m_YMax = 45f;  
      
        public float zMax { get { return m_ZMax; } set { m_ZMax = value; } }
        [[SerializeField](SerializeField.html)]
        float m_ZMax = 45f;  
      
        protected virtual void Start()
        {
            var joint = gameObject.AddComponent<[CharacterJoint](CharacterJoint.html)>();  
      
            var limit = joint.lowTwistLimit;
            limit.limit = m_XMin;
            joint.lowTwistLimit = limit;  
      
            limit = joint.highTwistLimit;
            limit.limit = m_XMax;
            joint.highTwistLimit = limit;  
      
            limit = joint.swing1Limit;
            limit.limit = m_YMax;
            joint.swing1Limit = limit;  
      
            limit = joint.swing2Limit;
            limit.limit = m_ZMax;
            joint.swing2Limit = limit;
        }
    }
    

The following Custom Editor example allows you to edit the serialized angular
limits in the Scene view.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.IMGUI.Controls;
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(JointExample)), [CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class JointExampleEditor : [Editor](Editor.html)
    {
        [JointAngularLimitHandle](IMGUI.Controls.JointAngularLimitHandle.html) m_Handle = new [JointAngularLimitHandle](IMGUI.Controls.JointAngularLimitHandle.html)();  
      
        // the OnSceneGUI callback uses the [Scene](SceneManagement.Scene.html) view camera for drawing handles by default
        protected virtual void OnSceneGUI()
        {
            var jointExample = (JointExample)target;  
      
            // copy the target object's data to the handle
            m_Handle.xMin = jointExample.xMin;
            m_Handle.xMax = jointExample.xMax;  
      
            // [CharacterJoint](CharacterJoint.html) and [ConfigurableJoint](ConfigurableJoint.html) implement y- and z-axes symmetrically
            m_Handle.yMin = -jointExample.yMax;
            m_Handle.yMax = jointExample.yMax;  
      
            m_Handle.zMin = -jointExample.zMax;
            m_Handle.zMax = jointExample.zMax;  
      
            // set the handle matrix to match the object's position/rotation with a uniform scale
            [Matrix4x4](Matrix4x4.html) handleMatrix = [Matrix4x4.TRS](Matrix4x4.TRS.html)(
                jointExample.transform.position,
                jointExample.transform.rotation,
                [Vector3.one](Vector3-one.html)
            );  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();  
      
            using (new [Handles.DrawingScope](Handles.DrawingScope.html)(handleMatrix))
            {
                // maintain a constant screen-space size for the handle's radius based on the origin of the handle matrix
                m_Handle.radius = [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html)([Vector3.zero](Vector3-zero.html));  
      
                // draw the handle
                [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
                m_Handle.DrawHandle();
                if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
                {
                    // record the target object before setting new values so changes can be undone/redone
                    [Undo.RecordObject](Undo.RecordObject.html)(jointExample, "Change [Joint](Joint.html) Example Properties");  
      
                    // copy the handle's updated data back to the target object
                    jointExample.xMin = m_Handle.xMin;
                    jointExample.xMax = m_Handle.xMax;  
      
                    jointExample.yMax = m_Handle.yMax == jointExample.yMax ? -m_Handle.yMin : m_Handle.yMax;  
      
                    jointExample.zMax = m_Handle.zMax == jointExample.zMax ? -m_Handle.zMin : m_Handle.zMax;
                }
            }
        }
    }
    

### Properties

[angleHandleDrawFunction](IMGUI.Controls.JointAngularLimitHandle-
angleHandleDrawFunction.html)| The CapFunction to use when displaying the
angle control handle.  
---|---  
[angleHandleSizeFunction](IMGUI.Controls.JointAngularLimitHandle-
angleHandleSizeFunction.html)| The SizeFunction to specify how large the angle
control handle should be.  
[fillAlpha](IMGUI.Controls.JointAngularLimitHandle-fillAlpha.html)| Returns or
specifies the opacity to use when rendering fill shapes for the range of
motion for each axis. Defaults to 0.1.  
[radius](IMGUI.Controls.JointAngularLimitHandle-radius.html)| Returns or
specifies the radius of the arc for the handle. Defaults to 1.0.  
[wireframeAlpha](IMGUI.Controls.JointAngularLimitHandle-wireframeAlpha.html)|
Returns or specifies the opacity to use for the curved lines along the outside
of the arcs of motion. Defaults to 1.0.  
[xHandleColor](IMGUI.Controls.JointAngularLimitHandle-xHandleColor.html)|
Returns or specifies the color to use for the handle limiting motion around
the x-axis. Defaults to Handles.xAxisColor.  
[xMax](IMGUI.Controls.JointAngularLimitHandle-xMax.html)| Returns or specifies
the maximum angular motion about the x-axis.  
[xMin](IMGUI.Controls.JointAngularLimitHandle-xMin.html)| Returns or specifies
the minimum angular motion about the x-axis.  
[xMotion](IMGUI.Controls.JointAngularLimitHandle-xMotion.html)| Returns or
specifies how angular motion is limited about the x-axis. Defaults to
ConfigurableJointMotion.Limited.  
[xRange](IMGUI.Controls.JointAngularLimitHandle-xRange.html)| Returns or
specifies the range of valid values for angular motion about the x-axis.
Defaults to [-180.0, 180.0].  
[yHandleColor](IMGUI.Controls.JointAngularLimitHandle-yHandleColor.html)|
Returns or specifies the color to use for the handle limiting motion around
the y-axis. Defaults to Handles.yAxisColor.  
[yMax](IMGUI.Controls.JointAngularLimitHandle-yMax.html)| Returns or specifies
the maximum angular motion about the y-axis.  
[yMin](IMGUI.Controls.JointAngularLimitHandle-yMin.html)| Returns or specifies
the minimum angular motion about the y-axis.  
[yMotion](IMGUI.Controls.JointAngularLimitHandle-yMotion.html)| Returns or
specifies how angular motion is limited about the y-axis. Defaults to
ConfigurableJointMotion.Limited.  
[yRange](IMGUI.Controls.JointAngularLimitHandle-yRange.html)| Returns or
specifies the range of valid values for angular motion about the y-axis.
Defaults to [-180.0, 180.0].  
[zHandleColor](IMGUI.Controls.JointAngularLimitHandle-zHandleColor.html)|
Returns or specifies the color to use for the handle limiting motion around
the z-axis. Defaults to Handles.zAxisColor.  
[zMax](IMGUI.Controls.JointAngularLimitHandle-zMax.html)| Returns or specifies
the maximum angular motion about the z-axis.  
[zMin](IMGUI.Controls.JointAngularLimitHandle-zMin.html)| Returns or specifies
the minimum angular motion about the z-axis.  
[zMotion](IMGUI.Controls.JointAngularLimitHandle-zMotion.html)| Returns or
specifies how angular motion is limited about the z-axis. Defaults to
ConfigurableJointMotion.Limited.  
[zRange](IMGUI.Controls.JointAngularLimitHandle-zRange.html)| Returns or
specifies the range of valid values for angular motion about the z-axis.
Defaults to [-180.0, 180.0].  
  
### Constructors

[JointAngularLimitHandle](IMGUI.Controls.JointAngularLimitHandle-ctor.html)|
Creates a new instance of the JointAngularLimitHandle class.  
---|---  
  
### Public Methods

[DrawHandle](IMGUI.Controls.JointAngularLimitHandle.DrawHandle.html)| A
function to display this instance in the current handle camera using its
current configuration.  
---|---  
  
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

