[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/install-existing-analyzer.html)
  * [中文](/cn/current/Manual/install-existing-analyzer.html)
  * [日本語](/ja/current/Manual/install-existing-analyzer.html)
  * [한국어](/kr/current/Manual/install-existing-analyzer.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/install-existing-analyzer.html)
  * [中文](/cn/current/Manual/install-existing-analyzer.html)
  * [日本語](/ja/current/Manual/install-existing-analyzer.html)
  * [한국어](/kr/current/Manual/install-existing-analyzer.html)

  * [Scripting](scripting.html)
  * [Debugging and diagnostics](debugging-and-diagnostics.html)
  * [Roslyn analyzers and source generators](roslyn-analyzers.html)
  * Install and use an existing analyzer or source generator

[](create-source-generator.html)

Create and use a source generator

[](ruleset-files.html)

Create rule set files

# Install and use an existing analyzer or source generator

This example uses the
[ErrorProne.NET.CoreAnalyzers](https://www.nuget.org/packages/ErrorProne.NET.CoreAnalyzers/)
library to demonstrate how to install code analyzers or source generators from
NuGet:

  1. Download the library as a .zip file with the **Download package** button.
  2. Extract the contents of the .zip file.
  3. Inside the extracted folder, locate the .dll files that contain the analyzers. In this example, navigate to **`errorprone.net.coreanalyzers<version-number>\analyzers\dotnet\cs`**. The required files should be in this folder, named `ErrorProne.NET.Core.dll`, `ErrorProne.Net.CoreAnalyzers.dll`, and `RuntimeContracts.dll`.
  4. Move these files into the Assets folder, or any folder nested inside of the Assets folder, in your Unity project. To do this, either go to **Assets** > **Import new asset** and select the .dll for each of the three files, or copy them into your project’s Assets folder through your device’s file browser.
  5. Click on the .dll file inside the **Asset Browser** inside Unity to open the **[Plugin Inspector](plug-in-inspector.html)** window.
  6. Inside the Plugin **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window:

     * Under the **Select platforms for plugin** heading, disable **Any Platform**.
     * Under the **Include Platforms** heading, disable **Editor** and **Standalone**.
  7. Under the **Asset Labels** heading in the Plugin Inspector window, click on the blue label icon to open the **Asset Labels** sub-menu.
  8. Create and assign a new label called RoslynAnalyzer. To do this, type `RoslynAnalyzer` into the text input window in the **Asset Labels** sub-menu and press **Return**. This label must exactly match the example and is case sensitive. After you create the label for the first analyzer, it appears on the list of available labels in the **Asset Labels** sub-menu. You can click on the name of the label in the menu to assign it to other analyzers.

Unity recognizes the RoslynAnalyzer label and treats assets with this label as
Roslyn Analyzers or source generators. When you assign the label to an
analyzer, Unity recompiles **scripts** A piece of code that allows you to
create your own Components, trigger game events, modify Component properties
over time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts) within the scope of the analyzer and
analyzes the code in those scripts according to the rules in the analyzer. Any
scripts that are within the same assembly definition as an analyzer are in
that analyzer’s scope. For analyzers in the root level of the Assets folder,
Unity considers all files in the project to be in scope. For more information
about scope, refer to [Analyzer scope and diagnostics](analyzer-scope-and-
diagnostics.html).

To test that your analyzers work correctly, follow the example below. If you
have installed the analyzers correctly, the ErrorProne.NET analyzer raises
warnings when it analyzes the code in the example.

Create a new script file named `RethrowError.cs`. Copy the following code into
this script and save the file:

    
    
    using System;
    using UnityEngine;
    
    public class RethrowError : MonoBehaviour
    {
        void Update()
        {
            try
            {
                DoSomethingInteresting();
            }
            catch (Exception e)
            {
                Debug.Log(e.Message);
                throw e;
            }
        }
    
        private void DoSomethingInteresting()
        {
            throw new System.NotImplementedException();
        }
    }
    

When you save the file, Unity recompiles the script and runs any applicable
analyzers on the script’s code. When the ErrorProne.NET analyzer is correctly
installed, it raises the following warnings in the **Console window** A Unity
Editor window that shows errors, warnings and other messages generated by
Unity, or your own scripts. [More info](Console.html)  
See in [Glossary](Glossary.html#Consolewindow) about the above code:

`Assets\RethrowError.cs(14,23): warning EPC12: Suspicious exception handling:
only e.Message is observed in exception block.`

`Assets\RethrowError.cs(15,19): warning ERP021: Incorrect exception
propagation. Use throw; instead.`

## Additional resources

  * [Create and use a source generator](create-source-generator.html)
  * [Create rule set files](ruleset-files.html)

[](create-source-generator.html)

Create and use a source generator

[](ruleset-files.html)

Create rule set files

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

