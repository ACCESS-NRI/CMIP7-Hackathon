# ACCESS-NRI’s CMIP7 Evaluation Hackathon Report
 
## Summary
 
From March 12-14, a group of climate modellers and developers gathered at CSIRO in Aspendale, Victoria for the CMIP7 ACCESS evaluation hackathon. The program involved a mix of presentations, discussions, and training sessions, alongside domain-specific breakout group discussions and hacking sessions. The primary goals from the organising committee’s perspective for the hackathon were to:
- Gather scientific input for ACCESS model evaluation at the model development stage
- Introduce the community to evaluation tools ESMValTool and ILAMB
- Agree upon desired metrics needed for evaluation to be incorporated into workflow “recipes” within these evaluation tools
- Build a community around the ACCESS model
- Discuss the type of simulations necessary and sufficient for evaluation of the model
 
The training and hackathon sessions focused on using ESMValTool – a community-driven workflow tool for evaluating Earth system models in CMIP. The ACCESS-NRI Model Evaluation and Diagnostics (MED) Team made ESMValTool available on the Gadi supercomputer at NCI, alongside relevant observational datasets ready to be used by the tool. The Gadi implementation specifically for the Australian ACCESS modelling community is called ESMValTool-workflow. Hackathon participants were introduced to ESMValTool-workflow and were challenged to start running recipes to gain familiarity with the tool. In addition, each domain-specific breakout group was asked to come up with a list of metrics that they use/need to evaluate their model, as well as a list of general issues/needs they would like ACCESS-NRI to address in relation to ACCESS model evaluation.
 
For more details about topics covered during the hackathon, you can read through the following notes taken by attendees (in Google Doc form):
- General hackathon notes (thanks to Sramana, Dhruv, and Aditya for these fantastic notes!)
- Domain-specific breakout group notes (these are condensed summaries of the discussions had in each breakout group, based on the notes taken by breakout group participants)

Other related documents, including the agenda and technical guides, can be found in the ACCESS-NRI CMIP7 Hackathon GitHub repository.
 
 
## Reflections and next steps from the ACCESS-NRI team
 
From the ACCESS-NRI perspective, the hackathon went very well, with good participant engagement. There were ~40 in-person and ~15 online attendees from the atmosphere, ocean/ice, land, and general/coupled domains, and participants were largely successful at running ESMValTool recipes on Gadi. The event also served as a learning exercise for ACCESS-NRI, where we got to hear feedback directly from model developers who were present. We had several overall takeaways:
- ESMValTool has a reasonable learning curve and we know that some participants found using the tool, as well as having to learn (for some) new tools like VS Code, to be difficult and frustrating.
  - The ACCESS-NRI MED team recognises the need to provide sustained support across all ACCESS communities to assist model developers adopt ESMValTool. Several MED team members are also involved in broader international ESMValTool community discussions and meetings and will advocate for the needs and desires of the Australian modeling community.
- Each community currently uses a mix of tools, including Python, NCL, and Ferret, to do their model evaluation. ESMValTool appears to be new to most of the ACCESS community.
  - The MED team is doing their best to provide support as people transition to ESMValTool, while also aiming to best meet the community where they are by incorporating as many previously-written recipes (e.g. using NCL or Xarray) into ESMValTool.
- ESMValTool requires input datasets (model and observations) to be CMORized. This posed some concerns among the participants as this is a barrier to using ESMValTool on ACCESS model output directly.
- Related to the above, there was a clear need from participants for the ability to model evaluation while the model is running and to be able to do quick diagnostics without the need to add the new step of CMORizing the data.
  - The MED team will be looking into options to CMORize data on the fly, while the model is running. They will also investigate hard coding in some evaluation diagnostics necessary for online model evaluation to be able to ingest raw ACCESS output, and potentially to compare to specific observational datasets. (It’s important to note, however, that each component of the ACCESS model – e.g. ocean, atmosphere – has its own model output format and file structure, so this will not be a straightforward task.)
- There is a clear desire from participants to be able to run ESMValTool in a Jupyter Notebook interface. This involves using the ESMValTool’s API, which exists, but is still a bit difficult to use due to lack of documentation. Additionally, the API allows users to call specific functions within ESMValTool, but it is written with the library Iris – a library similar to Xarray but with a much smaller user base. Most of the ACCESS community is far more familiar with Xarray than with Iris, and are hesitant to learn a new tool.
  - The MED team is prioritizing work on the API to allow for a smoother and less error-prone experience of using ESMValTool in Jupyter notebooks.
- The overall sentiment from participants at the event was positive, with several remarks about looking forward to similar events in the future.
  - The MED team agrees that it makes sense to run more similar events moving forward, and is looking into formats and timeframes for future events.
 
 
## Acknowledgements
 
The ACCESS-NRI team would like to thank the organizers of the hackathon for their immense efforts in putting together and running this event, and for accommodating both in-person and online participants. Their efforts in organizing the event itself allowed the ACCESS-NRI team to focus on preparing for the technical, hacking portions of the event, and so we are grateful for their time. We also recognize the funders of this event, CLEX - The ARC Centre of Excellence for Climate Extremes and ACCESS-NRI, and CSIRO Aspendale for hosting the in-person portion of the event.


*Note: this report was written from the ACCESS-NRI perspective and may not reflect all take-aways from the hackathon.*
