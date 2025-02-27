[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/VisualStudioIntegration.html)
  * [中文](/cn/current/Manual/VisualStudioIntegration.html)
  * [日本語](/ja/current/Manual/VisualStudioIntegration.html)
  * [한국어](/kr/current/Manual/VisualStudioIntegration.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/VisualStudioIntegration.html)
  * [中文](/cn/current/Manual/VisualStudioIntegration.html)
  * [日本語](/ja/current/Manual/VisualStudioIntegration.html)
  * [한국어](/kr/current/Manual/VisualStudioIntegration.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * Visual Studio C# integration

[](class-VersionControlSettings.html)

Version Control

[](RenderDocIntegration.html)

RenderDoc Integration

# Visual Studio C# integration

Unity integrates with Microsoft Visual Studio through the [Code Editor Package
for Visual
Studio](https://docs.unity3d.com/Packages/com.unity.ide.visualstudio@latest/).
This package is pre-installed when you install Unity. If Visual Studio is
installed at the time you install Unity, then Unity uses Visual Studio to open
and edit **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) by default.

![The Visual Studio Editor in the Package Manager Window](../uploads/Main/VS-
package.png) The Visual Studio Editor in the Package Manager Window

## Set Visual Studio as your default script editor

Unity automatically uses Visual Studio as its default script editor if Visual
Studio is installed when you install Unity, or if you install Visual Studio as
part of the Unity installation process. You can install Visual Studio as a
module into an existing Unity installation. For more information, see
[Downloading and installing Editors and modules with the Unity
Hub](https://docs.unity3d.com/hub/manual/InstallEditors.html).

To set your default script editor manually:

  * Go to **Edit > Preferences** (macOS: **Unity > Settings**) in the main menu to open the [Preferences window](Preferences.html).
  * Open the **External Tools** menu.
  * Click on the **External Script Editor** dropdown and select **Microsoft Visual Studio**. The appearance of this option changes depending on the version of Microsoft Visual Studio you have installed.

![External Tool Settings](../uploads/Main/VS-external-tools.png) External Tool
Settings

A: The External Script Editor dropdown menu, which displays the name and
version of the selected script editor.

B: The name and version of the Unity package that integrates with the selected
script editor.

Unity uses Visual Studio’s C# compiler to compile scripts. When you use the
Visual Studio Editor package with Visual Studio, both Unity and Visual Studio
display details of any errors in your scripts.

Unity automatically creates and maintains a Visual Studio .sln and .csproj
file. You can control whether Unity generates .csproj files for certain
elements of your project in the **External Tools** menu in the **Preferences**
window, as in the above screenshot. Enable or disable the checkboxes to toggle
whether Unity generates .csproj files for a given option.

Unity regenerates the .sln and .csproj files in your project whenever a
contributor makes changes to the state of a file, for example, editing an
existing file or creating a new one. You can also add files to your solution
from Visual Studio. Unity imports any new files, and the next time Unity
creates the project files again, it creates them with the new files included.

[](class-VersionControlSettings.html)

Version Control

[](RenderDocIntegration.html)

RenderDoc Integration

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

