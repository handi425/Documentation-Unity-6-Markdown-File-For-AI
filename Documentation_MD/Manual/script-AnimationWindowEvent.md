[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/script-AnimationWindowEvent.html)
  * [中文](/cn/current/Manual/script-AnimationWindowEvent.html)
  * [日本語](/ja/current/Manual/script-AnimationWindowEvent.html)
  * [한국어](/kr/current/Manual/script-AnimationWindowEvent.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/script-AnimationWindowEvent.html)
  * [中文](/cn/current/Manual/script-AnimationWindowEvent.html)
  * [日本語](/ja/current/Manual/script-AnimationWindowEvent.html)
  * [한국어](/kr/current/Manual/script-AnimationWindowEvent.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Animation clips](AnimationClips.html)
  * [Animation window](AnimationEditorGuide.html)
  * Add an Animation Event

[](animeditor-KeyManipulationInCurvesMode.html)

Key manipulation in Curves mode

[](BlendShapes.html)

Work with blend shapes

# Add an Animation Event

Use an **Animation Event** Allows you to add data to an imported clip which
determines when certain actions should occur in time with the animation. For
example, for an animated character you might want to add events to walk and
run cycles to indicate when the footstep sounds should play. [More
info](AnimationEventsOnImportedClips.html)  
See in [Glossary](Glossary.html#AnimationEvent) to call a function at a
specific point in time. This function can be in any script attached to the
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) but must only accept a single
parameter of type `float`, `int`, `string`, an `object` reference, or an
`AnimationEvent` object.

For example, the following script accepts a string. It logs the time and the
value of a string parameter when it is called.

    
    
    // An example of C# function that can be called by an Animation Event
    using UnityEngine;
    using System.Collections;
    
    public class ExampleClass : MonoBehaviour
    {
        public void PrintEvent(string s)
        {
            Debug.Log("PrintEvent called at " + Time.time + " with a value of " + s);
        }
    }
    

To add an Animation event to a clip at the current playhead location, click
the **Event** button. To add an Animation event at any position, right-click
the **Event** line where you want to add the Event and select **Add Animation
Event** from the context menu. Once added, click and drag an Animation event
to reposition it on the Event Line.

![Animation Events display on the Event
Line](../uploads/Main/AnimationEditorEventLine.png) **Animation Events**
display on the **Event Line**

When you add an Event, the **Inspector** A Unity window that displays
information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window displays the **Function**
field. Use this field to select the method you want to call. Note that
Animation Events only support methods with a single parameter. You cannot
select a function that accepts more than one parameter.

However, you can use an `AnimationEvent` object to pass many parameters at the
same time. An `AnimationEvent` object accepts a `float`, an `int`, a `string`,
and an `object` reference as member values. The `AnimationEvent` object also
provides information about the Animation Event that calls the function.

![The Inspector window with an Animation Event selected. The PrintEvent method
is selected from ExampleClass.](../uploads/Main/AnimationEventInspector.png)
The Inspector window with an Animation Event selected. The `PrintEvent` method
is selected from `ExampleClass`.

The Events added to a clip display as markers in the Event line. Hover the
cursor over a marker to display a tooltip with the function name and parameter
value.

![](../uploads/Main/AnimationEditorEventTooltip.png)

You can select and manipulate multiple Events in the Event Line. To select
multiple Events in the Event Line, hold the **Shift** key and click each Event
marker one by one. To remove a marker from the selection, hold **Shift** and
click a selected marker.

You can also use a selection box to select multiple Animation Events. To do
this, click and drag within the Event Line:

![](../uploads/Main/AnimationEditorMultipleEventSelection.png)

To delete an Animation Event, select it and press the **Delete** key. You can
also right-click the Animation Event and choose **Delete Event** from the
context menu.

[](animeditor-KeyManipulationInCurvesMode.html)

Key manipulation in Curves mode

[](BlendShapes.html)

Work with blend shapes

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

