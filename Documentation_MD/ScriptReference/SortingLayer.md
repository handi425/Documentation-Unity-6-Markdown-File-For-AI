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

# SortingLayer

struct in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

SortingLayer allows you to set the render order of multiple sprites easily.
There is always a default SortingLayer named "Default" which all sprites are
added to initially. Added more SortingLayers to easily control the order of
rendering of groups of sprites. Layers can be ordered before or after the
default layer.

Additional resources: [Tags and Layers](../Manual/class-TagManager.html).

### Static Properties

[layers](SortingLayer-layers.html)| Returns all the layers defined in this
project.  
---|---  
[onLayerAdded](SortingLayer-onLayerAdded.html)| Delegate for sorting layer
events when a layer is added.  
[onLayerRemoved](SortingLayer-onLayerRemoved.html)| Delegate for sorting layer
events when a layer is removed.  
  
### Properties

[id](SortingLayer-id.html)| This is the unique id assigned to the layer. It is
not an ordered running value and it should not be used to compare with other
layers to determine the sorting order.  
---|---  
[name](SortingLayer-name.html)| Returns the name of the layer as defined in
the TagManager.  
[value](SortingLayer-value.html)| This is the relative value that indicates
the sort order of this layer relative to the other layers.  
  
### Static Methods

[GetLayerValueFromID](SortingLayer.GetLayerValueFromID.html)| Returns the
final sorting layer value. To determine the sorting order between the various
sorting layers, use this method to retrieve the final sorting value and use
CompareTo to determine the order.  
---|---  
[GetLayerValueFromName](SortingLayer.GetLayerValueFromName.html)| Returns the
final sorting layer value. Additional resources: GetLayerValueFromID.  
[IDToName](SortingLayer.IDToName.html)| Returns the unique id of the layer.
Will return "<unknown layer>" if an invalid id is given.  
[IsValid](SortingLayer.IsValid.html)| Returns true if the id provided is a
valid layer id.  
[NameToID](SortingLayer.NameToID.html)| Returns the id given the name. Will
return 0 if an invalid name was given.  
  
### Delegates

[LayerCallback](SortingLayer.LayerCallback.html)| Calls the methods in its
invocation list when a sorting layer is added or removed.  
---|---  
  
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

