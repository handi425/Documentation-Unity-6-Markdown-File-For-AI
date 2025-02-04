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

#  [HandleUtility](HandleUtility.html).AddControl

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

public static void AddControl(int controlId, float distance);

### Parameters

controlId | The ID that is recorded as the nearest control if the mouse cursor is near the handle.  
---|---  
distance | The distance from the mouse cursor to the handle.  
  
### Description

Record a distance measurement from a handle.

All handles call this with their controlID during layout, then use
nearestControl to check if they got the mouseDown.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public float value = 1.0f;
    }
    
    // A tiny custom editor for ExampleScript component.
    [[CustomEditor](CustomEditor.html)(typeof(ExampleScript))]
    public class ExampleEditor : [Editor](Editor.html)
    {
        // Custom in-scene UI for when ExampleScript component is selected.
        public void OnSceneGUI()
        {
            var controlID = [GUIUtility.GetControlID](GUIUtility.GetControlID.html)([FocusType.Passive](FocusType.Passive.html));
            var evt = [Event.current](Event-current.html);
    
            var t = target as ExampleScript;
            var tr = t.transform;
            var pos = tr.position;
    
            switch (evt.GetTypeForControl(controlID))
            {
                case [EventType.Layout](EventType.Layout.html):
                case [EventType.MouseMove](EventType.MouseMove.html):
                    // Set the nearest control ID to "controlID" if the mouse cursor is
                    // near or directly above the solid disc handle.
                    var distanceToHandle = [HandleUtility.DistanceToCircle](HandleUtility.DistanceToCircle.html)(pos, t.value);
                    [HandleUtility.AddControl](HandleUtility.AddControl.html)(controlID, distanceToHandle);
                    break;
                case [EventType.MouseDown](EventType.MouseDown.html):
                    // Log the nearest control ID if the click is near or directly above
                    // the solid disc handle.
                    if (controlID == [HandleUtility.nearestControl](HandleUtility-nearestControl.html) && evt.button == 0)
                    {
                        [Debug.Log](Debug.Log.html)($"The nearest control is {controlID}.");
    
                        [GUIUtility.hotControl](GUIUtility-hotControl.html) = controlID;
                        evt.Use();
                    }
                    break;
                case [EventType.MouseUp](EventType.MouseUp.html):
                    if ([GUIUtility.hotControl](GUIUtility-hotControl.html) == controlID && evt.button == 0)
                    {
                        [GUIUtility.hotControl](GUIUtility-hotControl.html) = 0;
                        evt.Use();
                    }
                    break;
                case [EventType.Repaint](EventType.Repaint.html):
                    // [Display](Display.html) an orange solid disc where the object is.
                    [Handles.color](Handles-color.html) = new [Color](Color.html)(1, 0.8f, 0.4f, 1);
                    [Handles.DrawSolidDisc](Handles.DrawSolidDisc.html)(pos, tr.up, t.value);
                    break;
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

