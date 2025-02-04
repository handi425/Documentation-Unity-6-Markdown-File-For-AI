[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/EditingValueProperties.html)
  * [中文](/cn/current/Manual/EditingValueProperties.html)
  * [日本語](/ja/current/Manual/EditingValueProperties.html)
  * [한국어](/kr/current/Manual/EditingValueProperties.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/EditingValueProperties.html)
  * [中文](/cn/current/Manual/EditingValueProperties.html)
  * [日本語](/ja/current/Manual/EditingValueProperties.html)
  * [한국어](/kr/current/Manual/EditingValueProperties.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity's interface](UsingTheEditor.html)
  * Editing properties

[](InspectorFocused.html)

Focused Inspectors

[](Toolbar.html)

The Toolbar

# Editing properties

Properties are settings and options for **GameObject** The fundamental object
in Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) components and Assets. You edit
properties in an [Inspector window](UsingTheInspector.html).

![Light component showing various value and reference
properties](../uploads/Main/PropertiesExample.png) Light component showing
various value and reference properties

Properties fall into the following major categories:

  * **References:** links to other GameObjects and Assets.
  * **Values:** numbers, colors, on/off settings, text, and so on.

## References

Reference properties take compatible Project Assets or GameObjects in the
**Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) as inputs. For example, the [Mesh
Filter](class-MeshFilter.html)A mesh component that takes a mesh from your
assets and passes it to the Mesh Renderer for rendering on the screen. [More
info](class-MeshFilter.html)  
See in [Glossary](Glossary.html#MeshFilter) component refers to a
[Mesh](class-Mesh.html)The main graphics primitive of Unity. Meshes make up a
large part of your 3D worlds. Unity supports triangulated or Quadrangulated
polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons.
[More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Asset somewhere in the Project.

When you create a component, its reference properties are unassigned.

![](../uploads/Main/RefPropUnassigned.png)

You assign references to properties by dragging and dropping objects and
Assets onto reference property fields, or using an Object Picker window.

Some reference properties accept specific types of components (for example,
[Transform](class-Transform.html)). When you assign a GameObject to those
properties, Unity locates the first component of the required type on the
GameObject, and assigns it to the reference property. If the GameObject
doesn’t have any components of the right type, you cannot assign the
GameObject to the property.

### Assigning references by dragging and dropping

To assign a reference to a property, drag and drop a compatible GameObject or
Asset onto the property field in the Inspector.

![](../uploads/Main/inspector-refprop-dragdrop.png)

### Assigning references with the Object Picker window

Use the Object Picker window to find and select a reference object to assign.

![](../uploads/Main/inspector-refprop-picker.png)

  1. Click the small circle icon to the right of the property in the Inspector to open an Object Picker window.
  2. Find the object or Asset you want to reference, and double click it to assign it to the property.

## Values

You edit most value properties using simple controls. For example:

**Fields** where you enter text and numeric values.

![](../uploads/Main/inspector-property-numeric.png)

You can type numeric values directly in a property field, or click and drag
the property label to increase and decrease the value.

![](../uploads/Main/inspector-property-numeric-drag.png)

Some properties also have **sliders** for adjusting numeric values.

![](../uploads/Main/inspector-property-slider.png)

**Check boxes** where you toggle properties on and off.

![](../uploads/Main/inspector-property-checkbox.png)

**Drop-downs** and **pop-ups** where you choose one of multiple possible
values.

![](../uploads/Main/inspector-property-popup.png)

### Numeric field expressions

Numeric field input controls also accept mathematical expressions, for example
entering `2+3` into a field will result in value `5`. See
[ExpressionEvaluator](../ScriptReference/ExpressionEvaluator.html) C# class
documentation for details on which expressions are supported.

Numeric fields also support special functions that are useful when editing
multiple selected objects at once:

  * `L(a,b)` results in linear ramp between `a` and `b`.   
![](../uploads/Main/inspector-expr-L.png)  
_Entering`L(-6,6)` into X coordinate distributes the ten selected capsules
between –6 and 6._

  * `R(a,b)` results in a random value between `a` and `b`.   
![](../uploads/Main/inspector-expr-R.png)  
_Entering`R(-2,2)` into Z coordinate sets the Z coordinate of the selected
capsules to a random value between –2 and 2._

  * `+=`, `-=`, `*=`, `/=` expressions can be used to modify the current value, for example entering `*=2` makes all the the field value twice as large.   
![](../uploads/Main/inspector-expr-assign.png)  
_Entering`/=3` into Z coordinate makes all Z coordinates 3x smaller._

You can combine math expressions. For example, you could use the expression,
`L(0,2*pi)`, which produces a linear distribution of values between 0 and 2pi
radians, as the argument of a trigonometric function. To illustrate, the
following example uses this linear ramp function as the argument to sine and
cosine functions in order to distribute a set of selected objects in a circle:  
![](../uploads/Main/inspector-expr-trig.png)  
_Entering`cos(L(0,2*pi))*5` into X and `sin(L(0,2*pi))*5` into Z coordinates
places the ten selected capsules in a circle._

When writing [custom inspectors](editor-CustomEditors.html), all
[EditorGUI.PropertyField](../ScriptReference/EditorGUI.PropertyField.html) and
[EditorGUILayout.PropertyField](../ScriptReference/EditorGUILayout.PropertyField.html)
controls automatically get support for the numeric expressions.

Some GameObjects and Assets have more complex properties that you edit with
specialized controls or dedicated editors. The rest of this section describes
how to set these complex properties.

**Note** : Constrain Proportions Scale does not support math expressions for
multi-selection.

### Color values

The Inspector window displays color properties as swatches.

![](../uploads/Main/inspector-property-color.png)

Click any swatch to open a color picker or an **HDR** high dynamic range  
See in [Glossary](Glossary.html#HDR) color picker, depending on the context.
For example, Unity displays the HDR Color Picker window when you edit the
**emission** color property in the [standard shader](shader-
StandardShader.html).

![The Unity Color Picker window \(left\) and HDR color picker
\(right\)](../uploads/Main/color-pickers.png) The Unity Color Picker window
(left) and HDR color picker (right)

You can also use the eyedropper tool to pick color values from anywhere on the
screen.

![](../uploads/Main/inspector-property-color-eyedropper.png)

To pick a color, click the eyedropper button next to a color property, then
click anywhere on the screen. Unity sets the color property to the color of
the **pixel** The smallest unit in a computer image. Pixel size depends on
your screen resolution. Pixel lighting is calculated at every screen pixel.
[More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) you clicked.

You can save the colors you set in reusable swatch libraries that you can
share between projects.

### Gradient values

A gradient is a visual representation of a color progression. They are useful
for blending one color gradually into another, over space or time.

In Unity, gradient values are used by the [particle
system](PartSysColorOverLifeModule.html)A component that simulates fluid
entities such as liquids, clouds and flames by generating and animating large
numbers of small 2D images in the scene. [More info](class-
ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem), [line renderer](class-
LineRenderer.html)A component that takes an array of two or more points in 3D
space and draws a straight line between each one. You can use a single Line
Renderer component to draw anything from a simple straight line to a complex
spiral. [More info](class-LineRenderer.html)  
See in [Glossary](Glossary.html#LineRenderer) and a few other components. You
can also have public [Gradient class](../ScriptReference/Gradient.html)
variables in your C# **scripts** A piece of code that allows you to create
your own Components, trigger game events, modify Component properties over
time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts), and the inspector will display a
gradient editor for them.

![The Particle System gradient editor](../uploads/Main/inspector-gradient-
editor.png) The Particle System gradient editor

The gradient editor shows the main colors, called _keys_ , and all the
intermediate shades between them in the gradient bar (1).

Upward-pointing arrows along the bottom of the gradient bar represent color
keys (2).

  * Click a key to select it. Unity displays its color value in the **Color field**. 
    * Click the color swatch (3) to edit the color using a standard color picker.
    * You can also use the eyedropper tool (4) to pick color values from anywhere on the screen. Click the eyedropper button then click anywhere on the screen. Unity sets the color property to the color of the pixel you clicked.
  * Click an empty area under the gradient bar to add a key.
  * Click and drag a key to move it.
  * To delete a key, select it and use the **Ctrl/Cmd + Delete** shortcut.

Downward-pointing arrows above the gradient bar represent alpha keys (5) that
control the gradient’s transparency at a given point. You add and edit alpha
keys the same way you edit color keys. When you select an alpha key, the
gradient editor displays an **Alpha** slider instead of the **Color** field.

By default, a gradient has two keys set to 100% alpha, which makes the
gradient fully opaque. You can edit a key to adjust the transparency, and add
additional keys as needed.

A gradient can use several different color interpolation modes:

  * _Blend_ mode linearly interpolates between the color keys.
  * _Blend (Perceptual)_ mode interpolates between the color keys using a perceptually uniform “[Oklab](https://bottosson.github.io/posts/oklab/)” color space.
  * _Fixed_ mode does not interpolate the colors; the value of the color or alpha key is used until the next key.

![Blend gradient mode](../uploads/Main/GradientEditorModeBlend.png) Blend
gradient mode ![Perceptual blend gradient
mode](../uploads/Main/GradientEditorModePerceptual.png) Perceptual blend
gradient mode ![Fixed gradient
mode](../uploads/Main/GradientEditorModeFixed.png) Fixed gradient mode

### Curves

A **Curve** is a line graph that shows the response (on the y axis) to the
varying value of an input (on the x axis).

![The Curve editor in the Animation window](../uploads/Main/CurveEditor.png)
The Curve editor in the Animation window

Unity uses curves in a variety of different contexts, especially in animation.
Curve editors have a number of different options and tools. For details, see
[Editing Curves](EditingCurves.html).

### Bar sliders

A bar slider is a specialized control that lets you allocate a particular
resource visually. For example, the [LOD Group component](class-LODGroup.html)
uses a bar slider to define transitions between GameObject **LOD** The _Level
Of Detail_ (LOD) technique is an optimization that reduces the number of
triangles that Unity has to render for a GameObject when its distance from the
Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) levels.

![The LOD Group selection bar is a type of bar slider
control](../uploads/Main/LODGroup-SpeedTreeModels.png) The LOD Group selection
bar is a type of bar slider control

You adjust the relative values of each segment in the bar by dragging the
segment edges. Some bar sliders also have draggable handles.

### Arrays

When a script exposes an array as a public variable, the Inspector displays a
control that lets you edit both the number of items in the array (**Size**)
and the values or references within it.

![A script with a Vector3 array property](../uploads/Main/ArrayInspector.png)
A script with a Vector3 array property

When you decrease the **Size** value, Unity removes values from the end of the
array. When you increase the **Size** value, Unity copies the current last
value into all the new elements it adds.

Tip:  
---  
To set up an array whose values are mostly the same, add the first element and
then change the size to copy its value to subsequent elements.  
  
## Creating swatch libraries

Use swatch libraries to reuse, save, and share colors, gradients, and
**animation curves** Allows you to add data to an imported clip so you can
animate the timings of other items based on the state of an animator. For
example, for a game set in icy conditions, you could use an extra animation
curve to control the emission rate of a particle system to show the player’s
condensing breath in the cold air. [More
info](AnimationCurvesOnImportedClips.html)  
See in [Glossary](Glossary.html#AnimationCurves). You can save and choose
swatches in the Color Picker, Gradient Editor, and Curve Editor.

![Swatches section in the Unity Color
Picker](../uploads/Main/PresetLibrary.png) Swatches section in the Unity Color
Picker

A swatch library is a collection of swatches that you save in a file. The
Swatches section displays a single library at a time.

To save a swatch:

  1. Open the Color Picker, Gradient Editor, or Curve Editor. For example, select **Main Camera** in the [Hierarchy](Hierarchy.html) window.
  2. In the [Inspector](UsingTheInspector.html)A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window, click **Background Color**.

  3. In the picker window, adjust the color, gradient, or curve to your liking.
  4. In **Swatches** , click the outlined box.
  5. If the view is in List mode, optionally type a name for the swatch.

![Example of saving a color while in the Grid
view](../uploads/Main/SwatchSaving.png) Example of saving a color while in the
Grid view

Drag and drop swatches to change their order. Right-click a swatch to move it
to the top, replace it, rename it, or delete it. You can also delete a swatch
by Alt/Option-clicking it.

Use the drop-down menu in **Swatches** to:

  * Choose **List** or **Grid** to change the view. The List view also displays the names of swatches.
  * Choose a swatch library.
  * Choose **Create a Library** to create a new swatch library and the location to save it in.
  * Choose **Reveal Current Library Location** to view the current library in Windows Explorer/Mac OS Finder.

By default, Unity saves swatch libraries in your user preferences. You can
also save a swatch library in your Project. Unity saves Project swatch
libraries in the _Editor_ folder of the _Assets_ folder. To share Project
swatch libraries between users, or to include them in a package, add them to a
revision control repository.

To edit a Project swatch library:

  1. Select the swatch library in the [Project](ProjectView.html)In Unity, you use a project to design and develop a game. A project stores all of the files that are related to a game, such as the asset and Scene files. [More info](2Dor3D.html)  
See in [Glossary](Glossary.html#Project) window.

  2. In the [Inspector](UsingTheInspector.html) window, click **Edit**.

* * *

  * Reorganized Inspector section pages in Unity 2020.1

[](InspectorFocused.html)

Focused Inspectors

[](Toolbar.html)

The Toolbar

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

