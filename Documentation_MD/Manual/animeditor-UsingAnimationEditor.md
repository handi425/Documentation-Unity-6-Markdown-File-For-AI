[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/animeditor-UsingAnimationEditor.html)
  * [中文](/cn/current/Manual/animeditor-UsingAnimationEditor.html)
  * [日本語](/ja/current/Manual/animeditor-UsingAnimationEditor.html)
  * [한국어](/kr/current/Manual/animeditor-UsingAnimationEditor.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/animeditor-UsingAnimationEditor.html)
  * [中文](/cn/current/Manual/animeditor-UsingAnimationEditor.html)
  * [日本語](/ja/current/Manual/animeditor-UsingAnimationEditor.html)
  * [한국어](/kr/current/Manual/animeditor-UsingAnimationEditor.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Animation clips](AnimationClips.html)
  * [Animation window](AnimationEditorGuide.html)
  * Use the Animation view

[](AnimationEditorGuide.html)

Animation window

[](animeditor-CreatingANewAnimationClip.html)

Create a new Animation Clip

# Use the Animation view

Use the **Animation view** to preview and edit **Animation Clips** for
animated **GameObjects** in Unity. To open the Animation view in Unity, go to
**Window** > **Animation**.

## Viewing Animations on a GameObject

The **Animation window** is linked to the Hierarchy window, the **Project
window** A window that shows the contents of your `Assets` folder (Project
tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), the **Scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view, and the **Inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window. Like the Inspector, the
Animation window shows the timeline and **keyframes** A frame that marks the
start or end point of a transition in an animation. Frames in between the
keyframes are called inbetweens.  
See in [Glossary](Glossary.html#keyframe) of the Animation for the currently
selected **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) or **Animation Clip** Animation
data that can be used for animated characters or simple animations. It is a
simple “unit” piece of motion, such as (one specific instance of) “Idle”,
“Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) Asset. You can select a
GameObject using the Hierarchy window or the **Scene View** An interactive
view into the world you are creating. You use the Scene View to select and
position scenery, characters, cameras, lights, and all other types of Game
Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView), or select an Animation Clip Asset
using the Project Window.

## The Animated Properties list

In the image below, the Animation view (left) shows the Animation used by the
currently selected GameObject, and its child GameObjects if they are also
controlled by this Animation. The Scene view and Hierarchy view are on the
right, demonstrating that the Animation view shows the Animations attached to
the currently selected GameObject.

![](../uploads/Main/AnimationEditorShowsSelected.jpg)

In the left side of the Animation view is a list of the animated properties.
In a newly created clip where no animation has yet been recorded, this list is
empty.

![The Animation view displaying an empty clip. No properties are shown on the
left yet.](../uploads/Main/AnimationWindowEmptyClip.png) The Animation view
displaying an empty clip. No properties are shown on the left yet.

When you begin to animate various properties within this clip, the animated
properties will appear here. If the animation controls multiple child objects,
the list will also include hierarchical sub-lists of each child object’s
animated properties. In the example above, various parts of the Robot Arm’s
GameObject hierarchy are all animated within the same animation clip.

When animating a hierarchy of GameObjects within a single clip like this, make
sure you create the Animation on the root GameObject in the hierarchy.

Each property can be folded and unfolded to reveal the exact values recorded
at each keyframe. The value fields show the interpolated value if the playback
head (the white line) is between keyframes. You can edit these fields
directly. If changes are made when the playback head is over a keyframe, the
keyframe’s values are modified. If changes are made when the playback head is
between keyframes (and therefore the value shown is an interpolated value), a
new keyframe is created at that point with the new value that you entered.

## The Animation Timeline

On the right side of the Animation View is the timeline for the current clip.
The keyframes for each animated property appear in this timeline. The timeline
view has two modes, **Dopesheet** and **Curves**. To toggle between these
modes, click **Dopesheet** or **Curves** at the bottom of the animated
property list area:

![](../uploads/Main/AnimationEditorDopeSheetCurvesButtons.png)

These offer two alternate views of the Animation timeline and keyframe data.

### Dopesheet mode

**Dopesheet** mode offers a more compact view, allowing you to view each
property’s keyframe sequence in an individual horizontal track. This allows
you to view a simple overview of the keyframe timing for multiple properties
or GameObjects.

![Here the Animation Window is in Dope Sheet mode, showing the keyframe
positions of all animated properties within the Animation
clip](../uploads/Main/AnimationEditorDopeSheetView.png) Here the Animation
Window is in Dope Sheet mode, showing the keyframe positions of all animated
properties within the Animation clip

Consult [Key manipulation in Dopesheet mode](animeditor-
AdvancedKeySelectionAndManipulation.html) for more information.

### Curves mode

**Curves** mode displays a resizable graph containing a view of how the values
for each animated property changes over time. All selected properties appear
overlaid within the same graph view. This mode allows you to have great
control over viewing and editing the values, and how they are interpolated
between.

![Here, the Animation Window shows the curves for the rotation data of four
selected GameObjects within this Animation
clip](../uploads/Main/AnimationEditorCurvesViewMultipleSelected.png) Here, the
Animation Window shows the curves for the rotation data of four selected
GameObjects within this Animation clip

### Fitting your selection to the window

When using **Curves** mode to view your Animation, it’s important to
understand that sometimes the various ranges for each property can differ
greatly. For example, consider a simple Animation clip for a spinning bouncing
cube. The bouncing Y position value may vary between the range 0 to 2 (meaning
the cube bounces 2 units high during the animation); however, the rotation
value goes from 0 to 360 (representing its degrees of rotation). When viewing
these two curves at the same time, the **animation curves** Allows you to add
data to an imported clip so you can animate the timings of other items based
on the state of an animator. For example, for a game set in icy conditions,
you could use an extra animation curve to control the emission rate of a
particle system to show the player’s condensing breath in the cold air. [More
info](AnimationCurvesOnImportedClips.html)  
See in [Glossary](Glossary.html#AnimationCurves) for the position values will
be very difficult to make out because the view will be zoomed out to fit the
0–360 range of the rotation values within the window:

![The position and rotation curves of a bouncing spinning cube are both
selected, but because the view is zoomed out to fit the 0-360 range of the
rotation curve, the bouncing Y position curve is not easily
discernible](../uploads/Main/AnimationEditorTwoCurvesBigRangeDifference.png)
The position and rotation curves of a bouncing spinning cube are both
selected, but because the view is zoomed out to fit the 0–360 range of the
rotation curve, the bouncing Y position curve is not easily discernible

Press **F** on the keyboard to zoom the view to the currently selected
keyframes. This is useful as a quick way to focus and re-scale the window on a
portion of your Animation timeline for easier editing.

![](../uploads/Main/AnimationEditorSelectedKeyframesFitView.png)

Click on individual properties in the list and press **F** on the keyboard to
automatically re-scale the view to fit the range for that value. You can also
manually adjust the zoom of the **Curves** window by using the drag handles at
each end of the view’s scrollbar sliders. In the image below, the Animation
Window is zoomed in to view the bouncing Y position Animation. The start of
the yellow rotation curve is still visible, but now extends way off the top of
the view:

![](../uploads/Main/AnimationEditorTwoCurvesZoomedIn.png)

Press **A** on the keyboard to fit and re-scale the window to show all the
keyframes in the clip, regardless of which ones are selected. This is useful
if you want to view the whole timeline while preserving your current
selection:

![](../uploads/Main/AnimationEditorSelectedKeyframesAllView.png)

### Playback and frame navigation controls

To control playback of the **Animation Clip** , use the **Playback Controls**
at the top left of Animation view.

![Frame navigation](../uploads/Main/AnimationEditorFrameNavigation.png) Frame
navigation

From left-to-right, these controls are:

  * Preview mode (toggle on/off).
  * Record mode (toggle on/off). Note: Preview mode is on when record mode is on.
  * Move the playback head to the beginning of the clip.
  * Move the playback head to the previous keyframe.
  * Play the Animation Clip starting from the location of the playback head.
  * Move the playback head to the next keyframe.
  * Move the playback head to the end of the clip.
  * The location of the playback head in frames or seconds. Edit this field to move the playhead to a specific location.

You can also control the playback head with the following keyboard shortcuts:

  * Press Comma (,) to go to the previous frame or second.
  * Press Period (.) to go to the next frame or second.
  * Hold Alt (macOS: Option) and press Comma (,) to go to the previous keyframe.
  * Hold Alt (macOS: Option) and press Period (.) to go to the next keyframe.

### Locking the window

You can lock the Animation editor window so that it does not automatically
switch to reflect the currently selected GameObject in the Hierarchy or Scene.
Locking the window is useful if you want to focus on the Animation for one
particular GameObject, and still be able to select and manipulate other
GameObjects in the Scene.

![The Lock button](../uploads/Main/AnimationEditorWindowLockIcon.png) The Lock
button

To learn more about navigating the Curve view, consult [Using Animation
Curves](animeditor-AnimationCurves.html).

[](AnimationEditorGuide.html)

Animation window

[](animeditor-CreatingANewAnimationClip.html)

Create a new Animation Clip

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

