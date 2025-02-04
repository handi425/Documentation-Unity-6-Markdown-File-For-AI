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

#  [Input](Input.html).GetPenEvent

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

public static [PenData](PenData.html) GetPenEvent(int index);

### Returns

**PenData** Pen event details in the struct.

### Description

Returns the [PenData](PenData.html) for the pen event at the given index in
the pen event queue.

**Note: This API is part of the legacy** `Input` **class, and not recommended
for new projects. The documentation is provided here to support legacy
projects that use the old Input Manager and Input class. For new projects you
should use the newer and Input System Package**. ([read
more](../Manual/Input.html)).  
  
On Windows, the pen event queue holds, in chronological order, any missed pen
events as provided by GetPointerPenInfoHistory. The queue is cleared at the
end of each frame. On all other platforms the queue will always be empty.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class Example : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Window/Pen Window")]
        public static void ShowWindow()
        {
            [EditorWindow](EditorWindow.html) win = [EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(Example));
            win.titleContent = new [GUIContent](GUIContent.html)("Pen Window");
            win.wantsMouseMove = true;
        }  
      
        void OnGUI()
        {
            var e = [Event.current](Event-current.html);
            if ((e.type == [EventType.MouseDown](EventType.MouseDown.html)
                 || e.type == [EventType.MouseDrag](EventType.MouseDrag.html)
                 || e.type == [EventType.MouseDown](EventType.MouseDown.html)
                 || e.type == [EventType.MouseUp](EventType.MouseUp.html)
                 || e.type == [EventType.MouseMove](EventType.MouseMove.html))
                && (e.pointerType == [PointerType.Pen](PointerType.Pen.html)))
            {
                int count = [Input.penEventCount](Input-penEventCount.html);
                for (int i = 0; i < count; i++)
                {
                    // Log data from queued pen events
                    [PenData](PenData.html) p = [Input.GetPenEvent](Input.GetPenEvent.html)(i);
                    [Debug.Log](Debug.Log.html)($"Pen position {p.position}, pen pressure {p.pressure}, pen twist {p.twist}, pen tilt {p.tilt}, pen status - barrel {(p.penStatus & [PenStatus.Barrel](PenStatus.Barrel.html)) != 0}");
                }
                [Input.ResetPenEvents](Input.ResetPenEvents.html)();
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

