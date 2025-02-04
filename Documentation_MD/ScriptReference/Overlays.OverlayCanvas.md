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

# OverlayCanvas

class in UnityEditor.Overlays

Leave feedback

  

Implements
interfaces:[ISerializationCallbackReceiver](ISerializationCallbackReceiver.html)

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

OverlayCanvas is a container for collections of
[Overlay](Overlays.Overlay.html)s.

Every [EditorWindow](EditorWindow.html) has an
[OverlayCanvas](Overlays.OverlayCanvas.html), but only windows that opt-in to
Overlay support will display Overlays. See
[ISupportsOverlays](Overlays.ISupportsOverlays.html) for more information.

### Properties

[overlays](Overlays.OverlayCanvas-overlays.html)| The Overlays in this canvas.  
---|---  
[overlaysEnabled](Overlays.OverlayCanvas-overlaysEnabled.html)| Returns true
if overlays display in the window, or false if overlays are hidden.  
  
### Public Methods

[Add](Overlays.OverlayCanvas.Add.html)| Add an Overlay to this canvas. Added
Overlays will be displayed in the associated EditorWindow until they are
removed.  
---|---  
[OnAfterDeserialize](Overlays.OverlayCanvas.OnAfterDeserialize.html)| Invoked
after OverlayCanvas is deserialized.  
[OnBeforeSerialize](Overlays.OverlayCanvas.OnBeforeSerialize.html)| Invoked
before OverlayCanvas will be serialized. This is used to store Overlay layout
data.  
[Remove](Overlays.OverlayCanvas.Remove.html)| Remove an Overlay from this
canvas. Removed Overlays are disassociated from OverlayCanvas and the related
EditorWindow, but not destroyed. This means you are able to move a single
Overlay between multiple windows.  
[ResetOverlay](Overlays.OverlayCanvas.ResetOverlay.html)| Resets the overlay
to its default state.  
[RestoreOverlay](Overlays.OverlayCanvas.RestoreOverlay.html)| Restores Overlay
state according to the data parameter.  
[ShowPopup](Overlays.OverlayCanvas.ShowPopup.html)| Displays an overlay as a
pop-up in a EditorWindow.  
[ShowPopupAtMouse](Overlays.OverlayCanvas.ShowPopupAtMouse.html)| Displays an
overlay as a pop-up in a EditorWindow at the mouse position.  
  
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

