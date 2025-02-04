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

# Canvas

class in UnityEngine

/

Inherits from:[Behaviour](Behaviour.html)

/

Implemented in:[UnityEngine.UIModule](UnityEngine.UIModule.html)

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

Element that can be used for screen rendering.

Elements on a canvas are rendered AFTER Scene rendering, either from an
attached camera or using overlay mode.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.UI;  
      
    // Create a [Canvas](Canvas.html) that holds a Text [GameObject](GameObject.html).  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [GameObject](GameObject.html) myGO;
            [GameObject](GameObject.html) myText;
            [Canvas](Canvas.html) myCanvas;
            Text text;
            [RectTransform](RectTransform.html) rectTransform;  
      
            // [Canvas](Canvas.html)
            myGO = new [GameObject](GameObject.html)();
            myGO.name = "TestCanvas";
            myGO.AddComponent<[Canvas](Canvas.html)>();  
      
            myCanvas = myGO.GetComponent<[Canvas](Canvas.html)>();
            myCanvas.renderMode = [RenderMode.ScreenSpaceOverlay](RenderMode.ScreenSpaceOverlay.html);
            myGO.AddComponent<CanvasScaler>();
            myGO.AddComponent<GraphicRaycaster>();  
      
            // Text
            myText = new [GameObject](GameObject.html)();
            myText.transform.parent = myGO.transform;
            myText.name = "wibble";  
      
            text = myText.AddComponent<Text>();
            text.font = ([Font](Font.html))[Resources.Load](Resources.Load.html)("MyFont");
            text.text = "wobble";
            text.fontSize = 100;  
      
            // Text position
            rectTransform = text.GetComponent<[RectTransform](RectTransform.html)>();
            rectTransform.localPosition = new [Vector3](Vector3.html)(0, 0, 0);
            rectTransform.sizeDelta = new [Vector2](Vector2.html)(400, 200);
        }
    }
    

### Properties

[additionalShaderChannels](Canvas-additionalShaderChannels.html)| Get or set
the mask of additional shader channels to be used when creating the Canvas
mesh.  
---|---  
[cachedSortingLayerValue](Canvas-cachedSortingLayerValue.html)| Cached
calculated value based upon SortingLayerID.  
[isRootCanvas](Canvas-isRootCanvas.html)| Is this the root Canvas?  
[normalizedSortingGridSize](Canvas-normalizedSortingGridSize.html)| The
normalized grid size that the canvas will split the renderable area into.  
[overridePixelPerfect](Canvas-overridePixelPerfect.html)| Allows for nested
canvases to override pixelPerfect settings inherited from parent canvases.  
[overrideSorting](Canvas-overrideSorting.html)| Allows for nested canvases to
override the Canvas.sortingOrder from parent canvases.  
[pixelPerfect](Canvas-pixelPerfect.html)| Forces pixel alignment for elements
in the canvas. It only applies when Canvas.renderMode is set to Screen Space.  
[pixelRect](Canvas-pixelRect.html)| Get the render rect for the Canvas.  
[planeDistance](Canvas-planeDistance.html)| How far away from the camera is
the Canvas generated? It only applies when Canvas.renderMode is set to
RenderMode.ScreenSpaceCamera.  
[referencePixelsPerUnit](Canvas-referencePixelsPerUnit.html)| The number of
pixels per unit that is considered the default.  
[renderingDisplaySize](Canvas-renderingDisplaySize.html)| Returns the canvas
display size based on the selected render mode and target display.  
[renderMode](Canvas-renderMode.html)| Is the Canvas in World or Overlay mode?  
[renderOrder](Canvas-renderOrder.html)| The render order in which the canvas
is being emitted to the Scene. (Read Only)  
[rootCanvas](Canvas-rootCanvas.html)| Returns the Canvas closest to root, by
checking through each parent and returning the last canvas found. If no other
canvas is found then the canvas will return itself.  
[scaleFactor](Canvas-scaleFactor.html)| Scales the entire canvas, ensuring it
fits the screen. It only applies when Canvas.renderMode is set to Screen
Space.  
[sortingLayerID](Canvas-sortingLayerID.html)| Unique ID of the Canvas' sorting
layer.  
[sortingLayerName](Canvas-sortingLayerName.html)| Name of the Canvas' sorting
layer.  
[sortingOrder](Canvas-sortingOrder.html)| Canvas' order within a sorting
layer.  
[targetDisplay](Canvas-targetDisplay.html)| For Overlay mode, display index on
which the UI canvas will appear.  
[updateRectTransformForStandalone](Canvas-
updateRectTransformForStandalone.html)| Should the Canvas size be updated
based on the render target when a manual Camera.Render call is performed.  
[vertexColorAlwaysGammaSpace](Canvas-vertexColorAlwaysGammaSpace.html)| Should
the Canvas vertex color always be in gamma space before passing to the UI
shaders in linear color space work flow.  
[worldCamera](Canvas-worldCamera.html)|  Camera used for sizing the Canvas
when in Screen Space - Camera. Also used as the Camera that events will be
sent through for a World Space Canvas.  
  
### Static Methods

[ForceUpdateCanvases](Canvas.ForceUpdateCanvases.html)| Force all canvases to
update their content.  
---|---  
[GetDefaultCanvasMaterial](Canvas.GetDefaultCanvasMaterial.html)| Returns the
default material that can be used for rendering normal elements on the Canvas.  
[GetETC1SupportedCanvasMaterial](Canvas.GetETC1SupportedCanvasMaterial.html)|
Gets or generates the ETC1 Material.  
  
### Events

[preWillRenderCanvases](Canvas-preWillRenderCanvases.html)| Event that is
called just before Canvas rendering happens.  
---|---  
[willRenderCanvases](Canvas-willRenderCanvases.html)| Event that is called
just before Canvas rendering happens.  
  
### Inherited Members

### Properties

[enabled](Behaviour-enabled.html)| Enabled Behaviours are Updated, disabled
Behaviours are not.  
---|---  
[isActiveAndEnabled](Behaviour-isActiveAndEnabled.html)| Reports whether a
GameObject and its associated Behaviour is active and enabled.  
[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[BroadcastMessage](Component.BroadcastMessage.html)| Calls the method named
methodName on every MonoBehaviour in this game object or any of its children.  
---|---  
[CompareTag](Component.CompareTag.html)| Checks the GameObject's tag against
the defined tag.  
[GetComponent](Component.GetComponent.html)| Gets a reference to a component
of type T on the same GameObject as the component specified.  
[GetComponentInChildren](Component.GetComponentInChildren.html)| Gets a
reference to a component of type T on the same GameObject as the component
specified, or any child of the GameObject.  
[GetComponentIndex](Component.GetComponentIndex.html)| Gets the index of the
component on its parent GameObject.  
[GetComponentInParent](Component.GetComponentInParent.html)| Gets a reference
to a component of type T on the same GameObject as the component specified, or
any parent of the GameObject.  
[GetComponents](Component.GetComponents.html)| Gets references to all
components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](Component.GetComponentsInChildren.html)| Gets
references to all components of type T on the same GameObject as the component
specified, and any child of the GameObject.  
[GetComponentsInParent](Component.GetComponentsInParent.html)| Gets references
to all components of type T on the same GameObject as the component specified,
and any parent of the GameObject.  
[SendMessage](Component.SendMessage.html)| Calls the method named methodName
on every MonoBehaviour in this game object.  
[SendMessageUpwards](Component.SendMessageUpwards.html)| Calls the method
named methodName on every MonoBehaviour in this game object and on every
ancestor of the behaviour.  
[TryGetComponent](Component.TryGetComponent.html)| Gets the component of the
specified type, if it exists.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
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
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

