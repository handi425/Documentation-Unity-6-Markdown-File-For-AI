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

# IMGUIOverlay

class in UnityEditor.Overlays

/

Inherits from:[Overlays.Overlay](Overlays.Overlay.html)

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

IMGUIOverlay is an implementation of [Overlay](Overlays.Overlay.html) that
provides a [IMGUIContainer](UIElements.IMGUIContainer.html).

Inherit IMGUIOverlay to author [Overlay](Overlays.Overlay.html) elements
implemented using the legacy IMGUI controls.

### Public Methods

[CreatePanelContent](Overlays.IMGUIOverlay.CreatePanelContent.html)|
CreatePanelContent is invoked by the OverlayCanvas when this Overlay is shown.  
---|---  
[OnGUI](Overlays.IMGUIOverlay.OnGUI.html)| Implement IMGUI controls and logic
in this method.  
  
### Inherited Members

### Static Properties

[ussClassName](Overlays.Overlay-ussClassName.html)| USS class name of elements
of this type.  
---|---  
  
### Properties

[collapsed](Overlays.Overlay-collapsed.html)| Defines whether the overlay is
in collapsed form.  
---|---  
[collapsedIcon](Overlays.Overlay-collapsedIcon.html)| Defines a custom icon to
use when that overlay is in collapsed form.  
[containerWindow](Overlays.Overlay-containerWindow.html)| EditorWindow the
overlay is contained within.  
[defaultSize](Overlays.Overlay-defaultSize.html)| Set defaultSize to define
the size of an Overlay when it hasn't been resized by the user.  
[displayed](Overlays.Overlay-displayed.html)| Shows or hides the overlay.  
[displayName](Overlays.Overlay-displayName.html)| Name of overlay used as
title.  
[floating](Overlays.Overlay-floating.html)| Returns true if overlay is
floating, returns false if overlay is docked in a corner or in a toolbar.  
[floatingPosition](Overlays.Overlay-floatingPosition.html)| Local position of
closest overlay corner to closest dockposition when floating.  
[id](Overlays.Overlay-id.html)| Overlay unique ID.  
[isInToolbar](Overlays.Overlay-isInToolbar.html)| Returns true if overlay is
docked in a toolbar.  
[layout](Overlays.Overlay-layout.html)| The preferred layout for the Overlay.  
[maxSize](Overlays.Overlay-maxSize.html)| Maximum size of the Overlay.  
[minSize](Overlays.Overlay-minSize.html)| Minimum size of the Overlay.  
[rootVisualElement](Overlays.Overlay-rootVisualElement.html)| The root
VisualElement.  
[size](Overlays.Overlay-size.html)| Size of the Overlay.  
  
### Public Methods

[Close](Overlays.Overlay.Close.html)| Remove the Overlay from its
OverlayCanvas.  
---|---  
[CreateContent](Overlays.Overlay.CreateContent.html)| Creates a new
VisualElement containing the contents of this Overlay.  
[OnCreated](Overlays.Overlay.OnCreated.html)| OnCreated is invoked when an
Overlay is instantiated in an Overlay Canvas.  
[OnWillBeDestroyed](Overlays.Overlay.OnWillBeDestroyed.html)| Called when an
Overlay is about to be destroyed.  
[RefreshPopup](Overlays.Overlay.RefreshPopup.html)| Resize the OverlayPopup to
fit the content.  
[Undock](Overlays.Overlay.Undock.html)| If this Overlay is currently in a
toolbar, it will be removed and return to a floating state.  
  
### Events

[collapsedChanged](Overlays.Overlay-collapsedChanged.html)| Invoked when
Overlay.collapsed value is changed.  
---|---  
[displayedChanged](Overlays.Overlay-displayedChanged.html)| This callback is
invoked when the Overlay.displayed value has been changed.  
[floatingChanged](Overlays.Overlay-floatingChanged.html)| Called when the
value of floating has changed.  
[floatingPositionChanged](Overlays.Overlay-floatingPositionChanged.html)| This
event is invoked when Overlay.floatingPosition is changed.  
[layoutChanged](Overlays.Overlay-layoutChanged.html)| Subscribe to this event
to be notified when the Overlay.Layout property is modified.  
  
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

