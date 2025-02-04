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

# PanelSettings

class in UnityEngine.UIElements

/

Inherits from:[ScriptableObject](ScriptableObject.html)

/

Implemented
in:[UnityEngine.UIElementsModule](UnityEngine.UIElementsModule.html)

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

Defines a Panel Settings asset that instantiates a panel at runtime. The panel
makes it possible for Unity to display UXML-file based UI in the Game view.

### Properties

[bindingLogLevel](UIElements.PanelSettings-bindingLogLevel.html)|  Sets the
log level for bindings in panels using this PanelSettings asset.  
---|---  
[clearColor](UIElements.PanelSettings-clearColor.html)|  Determines whether
the color buffer is cleared before the panel is rendered.  
[clearDepthStencil](UIElements.PanelSettings-clearDepthStencil.html)|
Determines whether the depth/stencil buffer is cleared before the panel is
rendered.  
[colorClearValue](UIElements.PanelSettings-colorClearValue.html)|  The color
used to clear the color buffer.  
[depthClearValue](UIElements.PanelSettings-depthClearValue.html)|  The depth
used to clear the depth/stencil buffer.  
[dynamicAtlasSettings](UIElements.PanelSettings-dynamicAtlasSettings.html)|
Settings of the dynamic atlas.  
[fallbackDpi](UIElements.PanelSettings-fallbackDpi.html)|  The DPI value that
Unity uses when it cannot determine the screen DPI.  
[forceGammaRendering](UIElements.PanelSettings-forceGammaRendering.html)|
Forces the UI shader to output colors in the gamma color space.  
[match](UIElements.PanelSettings-match.html)|  Determines whether Unity uses
width, height, or a mix of the two as a reference when it scales the panel
area.  
[referenceDpi](UIElements.PanelSettings-referenceDpi.html)|  The DPI that the
UI is designed for.  
[referenceResolution](UIElements.PanelSettings-referenceResolution.html)|  The
resolution the UI is designed for.  
[referenceSpritePixelsPerUnit](UIElements.PanelSettings-
referenceSpritePixelsPerUnit.html)|  Sprites have a Pixels Per Unit value that
controls the pixel density of the sprite. For sprites that have the same
Pixels Per Unit value as the Reference Pixels Per Unit value in the
PanelSettings asset, the pixel density will be one to one.  
[scale](UIElements.PanelSettings-scale.html)|  A uniform scaling factor that
Unity applies to elements in the panel before the panel transform.  
[scaleMode](UIElements.PanelSettings-scaleMode.html)|  Determines how elements
in the panel scale when the screen size changes.  
[screenMatchMode](UIElements.PanelSettings-screenMatchMode.html)|  Specifies
how to scale the panel area when the aspect ratio of the current resolution
does not match the reference resolution.  
[sortingOrder](UIElements.PanelSettings-sortingOrder.html)|  When the Scene
uses more than one panel, this value determines where this panel appears in
the sorting order relative to other panels.  
[targetDisplay](UIElements.PanelSettings-targetDisplay.html)|  Set the display
intended for the panel.  
[targetTexture](UIElements.PanelSettings-targetTexture.html)|  Specifies a
Render Texture to render the panel's UI on.  
[textSettings](UIElements.PanelSettings-textSettings.html)|  Specifies a
PanelTextSettings that will be used by every UI Document attached to the
panel.  
[themeStyleSheet](UIElements.PanelSettings-themeStyleSheet.html)|  Specifies a
style sheet that Unity applies to every UI Document attached to the panel.  
[vertexBudget](UIElements.PanelSettings-vertexBudget.html)|  The expected
number of vertices that will be used by this panel.  
  
### Public Methods

[SetPanelChangeReceiver](UIElements.PanelSettings.SetPanelChangeReceiver.html)|
Sets a custom IPanelChangeReceiver in the panelChangeReceiver setter to
receive every change event. This method is available only in development
builds and the editor, as it is a debug feature to go along the profiling of
an application.  
---|---  
[SetScreenToPanelSpaceFunction](UIElements.PanelSettings.SetScreenToPanelSpaceFunction.html)|
Sets the function that handles the transformation from screen space to panel
space. For overlay panels, this function returns the input value.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
[CreateInstance](ScriptableObject.CreateInstance.html)| Creates an instance of
a scriptable object.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
### Messages

[Awake](ScriptableObject.Awake.html)| Called when an instance of
ScriptableObject is created.  
---|---  
[OnDestroy](ScriptableObject.OnDestroy.html)| This function is called when the
scriptable object will be destroyed.  
[OnDisable](ScriptableObject.OnDisable.html)| This function is called when the
scriptable object goes out of scope.  
[OnEnable](ScriptableObject.OnEnable.html)| This function is called when the
object is loaded.  
[OnValidate](ScriptableObject.OnValidate.html)| Editor-only function that
Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](ScriptableObject.Reset.html)| Reset to default values.  
  
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

