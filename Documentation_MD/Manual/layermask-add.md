[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/layermask-add.html)
  * [中文](/cn/current/Manual/layermask-add.html)
  * [日本語](/ja/current/Manual/layermask-add.html)
  * [한국어](/kr/current/Manual/layermask-add.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/layermask-add.html)
  * [中文](/cn/current/Manual/layermask-add.html)
  * [日本語](/ja/current/Manual/layermask-add.html)
  * [한국어](/kr/current/Manual/layermask-add.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with scenes](working-with-scenes.html)
  * [Layers](Layers.html)
  * [Layers and layerMasks](layers-and-layermasks.html)
  * Add a layer to a layerMask

[](layermask-set.html)

Set a layerMask

[](layermask-remove.html)

Remove a layer from a layerMask

# Add a layer to a layerMask

To add a layer to a layermask, use the [logical OR
operator](https://docs.microsoft.com/en-us/dotnet/csharp/language-
reference/operators/bitwise-and-shift-operators#logical-or-operator-) on the
original layermask and the layer to add.

    
    
    originalLayerMask |= (1 << layerToAdd);
    

## Additional resources

  * [Set a layermask](layermask-set.html)
  * [Remove a layer from a layermask](layermask-remove.html)

[](layermask-set.html)

Set a layerMask

[](layermask-remove.html)

Remove a layer from a layerMask

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

