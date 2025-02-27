[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UsingComponents.html)
  * [中文](/cn/current/Manual/UsingComponents.html)
  * [日本語](/ja/current/Manual/UsingComponents.html)
  * [한국어](/kr/current/Manual/UsingComponents.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UsingComponents.html)
  * [中文](/cn/current/Manual/UsingComponents.html)
  * [日本語](/ja/current/Manual/UsingComponents.html)
  * [한국어](/kr/current/Manual/UsingComponents.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Components](unity-components.html)
  * Use components

[](Components.html)

Introduction to components

[](CreatingComponents.html)

Create components with scripts

# Use components

You can use different components to change or add functions to your
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject). You can use the **Inspector** A
Unity window that displays information about the currently selected
GameObject, asset or project settings, allowing you to inspect and edit the
values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window to change the properties of
any component, or you can use **scripts** A piece of code that allows you to
create your own Components, trigger game events, modify Component properties
over time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts).

For more information on how to use your components with scripts, see the
[components script
reference](https://docs.unity3d.com/2022.2/Documentation/ScriptReference/Component.html)
page.

## Add components

You can add components to the selected GameObject through the Component menu.
To add a Rigidbody component, select the GameObject and select **Component** >
**Physics** > **Rigidbody** from the menu. The Inspector displays the
Rigidbody’s properties. If you press **Play** while you have the empty
GameObject selected, the Y position of the GameObject’s transform decreases.
This is because the physics system in Unity causes the GameObject to fall
under gravity.

![A GameObject with a Rigidbody component
attached](../uploads/Main/RigidBodyGO1.png) A GameObject with a Rigidbody
component attached

You can also add components in the **Component** browser. To open the
Component browser, select **Add Component** in the Inspector.

![The Component browser](../uploads/Main/ComponentBrowser1.png) The Component
browser

You can navigate the components by category in the browser or use the search
box to locate components by name.

You can attach any number or combination of components to a single GameObject.
Some components work best in combination with others. For example, the
Rigidbody works with a **Collider** An invisible shape that is used to handle
physical collisions for an object. A collider doesn’t need to be exactly the
same shape as the object’s mesh - a rough approximation is often more
efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider).

For more information about a particular component, see the relevant Component
reference page. You can also access the reference page for a component from
Unity if you select the help icon (**?**) on the component’s header in the
Inspector.

## Edit components

When you attach a component to a GameObject, the component’s properties
contain default values. You can edit these values in the Editor while you
build a game, or in scripts when you run the game.

There are two main types of properties: values and references.

You can edit value properties in the Inspector. There are various types of
values, including text, toggles and dropdowns.

For reference properties, you can drag a file from the Project view into the
property, or use the object picker (circle icon) on the property. Reference
properties can reference other types of components, GameObjects, or assets.

For more information about the different property types, see [Editing
Properties](EditingValueProperties.html).

The image below shows a GameObject with an ****Audio Source** A component
which plays back an Audio Clip in the scene to an audio listener or through an
audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource)** component. The values of the
**Audio Source** in the Inspector show how you can adjust aspects of a
component to suit your project.

![The Audio Source with a sound effect referenced properly in the Audio
Clip](../uploads/Main/AudioReference1.png) The Audio Source with a sound
effect referenced properly in the Audio Clip

## Component context menu commands

Right click on a component for the context menu with several useful commands.

The same commands are also available from the kebab menu (⋮) in the top-right
of the component panel in the Inspector window.

The table below describes the commands available so you can adjust your
components:

**Command:** | **Description:**  
---|---  
**Reset** | Restores the values the component’s properties had before the most recent editing session.  
**Remove Component** | Removes the component from the GameObject. **Note** : Some combinations of components depend on each other ([Hinge Joint](class-HingeJoint.html)A joint that groups together two Rigidbody components, constraining them to move like they are connected by a hinge. It is perfect for doors, but can also be used to model chains, pendulums and so on. [More info](class-HingeJoint.html)  
See in [Glossary](Glossary.html#HingeJoint) only works when attached to a
[Rigidbody](class-Rigidbody.html)A component that allows a GameObject to be
affected by simulated gravity and other forces. [More info](class-
Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody)); a warning message is displayed if
you try to remove components that others depend on.  
**Move Up** | Moves the component up in the Inspector. You can also drag and drop components in the Inspector to reorder them.  
**Move Down** | Moves the component down in the Inspector.  
**Copy Component** | Copies the type and current property settings of a component.  
**Paste Component As New** | Pastes the copied property settings of a component as a new component.  
**Paste Component Values** | Pastes the copied property settings of a component into another component of the same type.  
  
## Testing properties

In **Play Mode** , you can change properties of a component in the Inspector.
This lets you see how different values for a property affect gameplay. For
example, you can experiment with different heights of jumping. If you create a
**Jump Height** property in a script, you can enter Play Mode, change the
value, and press the jump button to see what happens. Then, without exiting
Play Mode, you can change it again and see the results within seconds. When
you exit Play Mode, the properties revert to their pre-Play Mode values. With
this workflow, you can experiment, adjust, and refine your gameplay in less
time.

[](Components.html)

Introduction to components

[](CreatingComponents.html)

Create components with scripts

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

