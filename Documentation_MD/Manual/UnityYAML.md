[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityYAML.html)
  * [中文](/cn/current/Manual/UnityYAML.html)
  * [日本語](/ja/current/Manual/UnityYAML.html)
  * [한국어](/kr/current/Manual/UnityYAML.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityYAML.html)
  * [中文](/cn/current/Manual/UnityYAML.html)
  * [日本語](/ja/current/Manual/UnityYAML.html)
  * [한국어](/kr/current/Manual/UnityYAML.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * [Text-Based Scene Files](TextSceneFormat.html)
  * UnityYAML

[](FormatDescription.html)

Format of Text Serialized files

[](YAMLSceneExample.html)

An Example of a YAML Scene File

# UnityYAML

Unity uses a custom-optimized YAML library called UnityYAML. The UnityYAML
library does not support the [full YAML
specification](https://yaml.org/spec/). This documentation outlines which
parts of the YAML spec UnityYAML supports.

You cannot externally produce or edit UnityYAML files.

## Supported features

**Feature** | **Support**  
---|---  
**Mappings** | UnityYAML supports both flow and block styles.  
**Scalars** | UnityYAML supports double and single quoted scalars as well as plain scalars. You can split them onto multiple lines. Be aware that multi-line scalars can create performance and memory overheads during parsing.  
  
Plain scalars split onto multiple lines must be indented more than the
previous line. See below this table for an example.  
  
You can use UTF–8 characters in scalars, but UnityYAML only decodes them when
they are part of a double quoted scalar.  
**Sequences** | UnityYAML supports mapping, block styles, and block sequences that contain block mappings.  
  
### Example of indentation on multi-line plain scalars:

    
    
    parent: This is a
      multi-line scalar
    ^
    |
    

If there is no indentation, the scalar returns `This is a` and might trigger
an Asset into further parsing.

## Unsupported features

**Feature** | **Support**  
---|---  
**Chomping indicators** | UnityYAML does not support using `+` and `|` characters to indicate how it should treat new lines within a multi-line string. If you use these characters, UnityYAML adds them to the scalar value.  
**Comments** | UnityYAML does not support comments.  
**Complex mapping keys** | UnityYAML does not support complex mapping keys.  
**Multiple documents** | The reader skips document and tag prefixes at the top of files, but does not handle YAML input that consists of multiple documents.  
**Raw block sequences** | Nearly all nodes are part of a mapping in UnityYAML, so all sequences must be values of a mapping to work correctly. See below this table for an example.  
  
Anonymous sequences increase the parser complexity. You cannot use indentation
as a way of determining if a sequence element has finished in UnityYAML.  
**Tags** A reference word which you can assign to one or more GameObjects to
help you identify GameObjects for scripting purposes. For example, you might
define and “Edible” Tag for any item the player can eat in your game. [More
info](Tags.html)  
See in [Glossary](Glossary.html#Tag) | UnityYAML does not support tags.  
  
### Example of a raw block sequence

    
    
    var:
      - 1
      - 2
      - 3
    

The sequence is designed for lookups upon `var`, so the following does not
work:

    
    
    - 1
    - 2
    - 3
    

* * *

  * 2019–05–13 Page published 

  * New in [2019.3](https://docs.unity3d.com/2019.3/Documentation/Manual/30_search.html?q=newin20193) NewIn20193

[](FormatDescription.html)

Format of Text Serialized files

[](YAMLSceneExample.html)

An Example of a YAML Scene File

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

