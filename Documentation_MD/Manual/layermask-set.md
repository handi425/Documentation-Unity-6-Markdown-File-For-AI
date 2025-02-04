[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/layermask-set.html)
  * [中文](/cn/current/Manual/layermask-set.html)
  * [日本語](/ja/current/Manual/layermask-set.html)
  * [한국어](/kr/current/Manual/layermask-set.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/layermask-set.html)
  * [中文](/cn/current/Manual/layermask-set.html)
  * [日本語](/ja/current/Manual/layermask-set.html)
  * [한국어](/kr/current/Manual/layermask-set.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with scenes](working-with-scenes.html)
  * [Layers](Layers.html)
  * [Layers and layerMasks](layers-and-layermasks.html)
  * Set a layerMask

[](layermask-introduction.html)

Introduction to layerMasks

[](layermask-add.html)

Add a layer to a layerMask

# Set a layerMask

This page explains how to set up a layerMask correctly so you can use it in
API calls that use a serialized layerMask property.

## Use a serialized layerMask property

The simplest way to set a layermask in the Unity Editor is to create a
property that uses Unity’s [LayerMask](../ScriptReference/LayerMask.html)
class. If the property is `public` or uses the
[SerializeField](../ScriptReference/SerializeField.html) attribute, Unity
provides an interface in the **Inspector** A Unity window that displays
information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) that you can use to select which
layers the layermask represents.

    
    
    using UnityEngine;
    
    public class LayerMaskExample : MonoBehaviour
    {
        [SerializeField] private LayerMask layermask;
    }
    

## Convert from a layer

If you want to convert a layer to a layermask in a script at runtime, use the
[binary left-shift operator](https://docs.microsoft.com/en-
us/dotnet/csharp/language-reference/operators/bitwise-and-shift-
operators#left-shift-operator-) to left-shift `1` by the layer. The result is
a layermask that represents the single layer.

    
    
    using UnityEngine;
    
    public class LayerExample : MonoBehaviour
    {
        [SerializeField] private int layer = 10;
        private int layerAsLayerMask;
    
        private void Start()
        {
            layerAsLayerMask = (1 << layer);
        }
    }
    

## Additional resources

  * [Add a layer to a layermask](layermask-add.html)
  * [Remove a layer from a layermask](layermask-remove.html)

[](layermask-introduction.html)

Introduction to layerMasks

[](layermask-add.html)

Add a layer to a layerMask

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

